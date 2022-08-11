import os
import pandas as pd
from scipy import interpolate


class SolidProps(object):
    def __init__(self, material):
        """ class for interfacing material properties of solids """
        self._set_df(material)
        self.interp_K = self._get_interpolator('K/(W/(m.K))')
        self.interp_cp = self._get_interpolator('cp/(J/(kg.K))')
        self.interp_alpha_th = self._get_interpolator('alpha_thermal/(1/K)')
        self.interp_elec_resistivity = self._get_interpolator('resistivity/(ohm.m)')

    def _set_df(self, material):
        d = {'AL5083': 'ALUMINUM_ALLOY_5083-T0.csv',
             'AL6061': 'ALUMINUM_ALLOY_6061-T6.csv',
             'AL': 'ALUMINUM_PURE.csv',
             'ALUMINUM': 'ALUMINUM_PURE.csv',
             'AU': 'GOLD_PURE.csv',
             'BRASS': 'COPPER_ZINC_90_10.csv',
             'CARBON_FIBER_NORMAL': 'CARBON_FIBER_NORMAL_TO_FIBER.csv',
             'CARBON_FIBER_PARALLEL': 'CARBON_FIBER_PARALLEL.csv',
             'COPPER': 'COPPER_PURE.csv',
             'COPPER-NICKEL_57-43': 'COPPER-NICKEL_57-43.csv',
             'COPPER-NICKEL_70-30': 'COPPER-NICKEL_70-30.csv',
             'COPPER-NICKEL_90-10': 'COPPER-NICKEL_90-10.csv',
             'COPPER-ZINC_90-10': 'COPPER_ZINC_90_10.csv',
             'CU': 'COPPER_PURE.csv',
             'CU-NI_57-43': 'COPPER-NICKEL_57-43.csv',
             'CU-NI_70-30': 'COPPER-NICKEL_70-30.csv',
             'CU-NI_90-10': 'COPPER-NICKEL_90-10.csv',
             'CZ-ZN_90-10': 'COPPER_ZINC_90_10.csv',
             'CUPRONICKEL_57-43': 'COPPER-NICKEL_57-43.csv',
             'CUPRONICKEL_70-30': 'COPPER-NICKEL_70-30.csv',
             'CUPRONICKEL_90-10': 'COPPER-NICKEL_90-10.csv',
             'EPOXY': 'EPOXY.csv',
             'G10_NORMAL_TO_CLOTH': 'G10_NORMAL_TO_CLOTH.csv',
             'G10_PARALLEL_TO_FILL': 'G10_PARALLEL_TO_FILL.csv',
             'G10_PARALLEL_TO_WRAP': 'G10_PARALLEL_TO_WRAP.csv',
             'GOLD': 'GOLD_PURE.csv',
             'INVAR': 'INVAR-36.csv',
             'INVAR-36': 'INVAR-36.csv',
             'LEAD': 'LEAD_PURE.csv',
             'KAPTON': 'KAPTON.csv',
             'PB': 'LEAD_PURE.csv',
             'SAPPHIRE': 'SAPPHIRE_PURE.csv',
             'SS304L': 'STAINLESS_STEEL_304L.csv',
             'SS310L': 'STAINLESS_STEEL_310L.csv',
             'TI': 'TITANIUM_PURE.csv',
             'TITANIUM': 'TITANIUM_PURE.csv'}
        if material.upper() not in d.keys():
            raise TypeError(f'Unknown properties of {material}')
        location = os.path.dirname(os.path.realpath(__file__))
        data = os.path.join(location, 'lib', d[material.upper()])
        self.df = pd.read_csv(data, sep = r',', engine='python')

    def _get_interpolator(self, prop):
        return interpolate.interp1d(self.df['T/K'], self.df[prop])

    def check_T_in_range(self, T):
        assert T >= 1.0, f"Temperature {T} K below the 1 K limit"
        assert T <= 300.0, f"Temperature {T} K above the 300 K limit"

    def get_rhomass(self, T=200):
        """ return density in (kg/m^3) """
        self.check_T_in_range(T)
        return float(self.df['rho/(kg/m3)'][0])

    def get_K(self, T):
        """ return thermal conductivity in (W/(m.K)) """
        self.check_T_in_range(T)
        return float(self.interp_K(T))

    def get_cp(self, T):
        """ return specific heat in (J/(kg.K)) """
        self.check_T_in_range(T)
        return float(self.interp_cp(T))

    def get_cv(self, T):
        """
        return Cv in (J/(kg.K))
        for incrompressible substances Cp = Cv
        """
        return self.get_cp(T)

    def get_thermal_expansion_coefficient(self, T):
        """ return thermal expansion coefficient in (1/K) """
        self.check_T_in_range(T)
        return float(self.interp_alpha_th(T))

    def get_thermal_diffusivity(self, T):
        """ return thermal diffusivity in (m^2/s) """
        self.check_T_in_range(T)
        return self.get_K(T) / self.get_rhomass() / self.get_cp(T)

    def get_electrical_resistivity(self, T):
        """ return resistivity in (ohm.m) """
        self.check_T_in_range(T)
        return float(self.interp_elec_resistivity(T))