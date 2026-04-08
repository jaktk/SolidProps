from .SolidProps import SolidProps, available_materials

__version__ = '1.1'


def get_K(material, T):
    """ return thermal conductivity in (W/(m.K)) for given material and temperature """
    return SolidProps(material).get_K(T)


def get_cp(material, T):
    """ return specific heat in (J/(kg.K)) for given material and temperature """
    return SolidProps(material).get_cp(T)


def get_cv(material, T):
    """ return Cv in (J/(kg.K)) for given material and temperature """
    return SolidProps(material).get_cv(T)


def get_rhomass(material):
    """ return density in (kg/m^3) for given material """
    return SolidProps(material).get_rhomass()


def get_thermal_expansion_coefficient(material, T):
    """ return thermal expansion coefficient in (1/K) for given material and temperature """
    return SolidProps(material).get_thermal_expansion_coefficient(T)


def get_thermal_diffusivity(material, T):
    """ return thermal diffusivity in (m^2/s) for given material and temperature """
    return SolidProps(material).get_thermal_diffusivity(T)


def get_electrical_resistivity(material, T):
    """ return electrical resistivity in (ohm.m) for given material and temperature """
    return SolidProps(material).get_electrical_resistivity(T)
