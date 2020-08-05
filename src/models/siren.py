from typing import Tuple

import torch
import torch.nn as nn

import numpy as np
from collections import OrderedDict


class SineLayer(nn.Module):
    """
    Copied from original Colab Notebook. Sine Layer, basic layer
    of Siren network
    """

    def __init__(
            self,
            in_features: int,
            out_features: int,
            bias: bool = True,
            is_first: bool = False,
            omega_0: float = 30
    ):
        super().__init__()
        self.omega_0 = omega_0
        self.is_first = is_first

        self.in_features = in_features
        self.linear = nn.Linear(in_features, out_features, bias=bias)

        self.init_weights()

    def init_weights(self):
        with torch.no_grad():
            if self.is_first:
                self.linear.weight.uniform_(
                    -1 / self.in_features,
                    1 / self.in_features
                )
            else:
                self.linear.weight.uniform_(
                    -np.sqrt(6 / self.in_features) / self.omega_0,
                    np.sqrt(6 / self.in_features) / self.omega_0
                )

    def forward(self, x: torch.Tensor):
        return torch.sin(self.omega_0 * self.linear(x))

    def forward_with_intermediate(self, x: torch.Tensor):
        # For visualization of activation distributions
        intermediate = self.omega_0 * self.linear(x)
        return torch.sin(intermediate), intermediate


class Siren(nn.Module):
    def __init__(
            self,
            in_features: int,
            hidden_features: int,
            hidden_layers: int,
            out_features: int,
            outermost_linear: bool = False,
            first_omega_0:  float = 30,
            hidden_omega_0: float = 30,
    ) -> None:
        super().__init__()

        self.net = []
        self.net.append(SineLayer(in_features, hidden_features,
                                  is_first=True, omega_0=first_omega_0))

        for i in range(hidden_layers):
            self.net.append(SineLayer(hidden_features, hidden_features,
                                      is_first=False, omega_0=hidden_omega_0))

        if outermost_linear:
            final_linear = nn.Linear(hidden_features, out_features)

            with torch.no_grad():
                final_linear.weight.uniform_(
                    -np.sqrt(6 / hidden_features) / hidden_omega_0,
                    np.sqrt(6 / hidden_features) / hidden_omega_0
                )

            self.net.append(final_linear)
        else:
            self.net.append(SineLayer(hidden_features, out_features,
                                      is_first=False, omega_0=hidden_omega_0))

        self.net = nn.Sequential(*self.net)

    def forward(
            self, coords: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        coords = coords.clone().detach().requires_grad_(
            True)  # allows to take derivative w.r.t. input
        output: torch.Tensor = self.net(coords)
        return output, coords

    def forward_with_activations(
            self,
            coords: torch.Tensor,
            retain_grad: bool = False,
    ) -> OrderedDict:
        """Returns not only model output, but also intermediate activations.
        Only used for visualizing activations later!"""
        activations = OrderedDict()

        activation_count = 0
        x = coords.clone().detach().requires_grad_(True)
        activations['input'] = x
        for i, layer in enumerate(self.net):
            if isinstance(layer, SineLayer):
                x, intermed = layer.forward_with_intermediate(x)

                if retain_grad:
                    x.retain_grad()
                    intermed.retain_grad()

                activations['_'.join((str(layer.__class__),
                                      "%d" % activation_count))] = intermed
                activation_count += 1
            else:
                x = layer(x)

                if retain_grad:
                    x.retain_grad()

            activations[
                '_'.join((str(layer.__class__), "%d" % activation_count))] = x
            activation_count += 1

        return activations
