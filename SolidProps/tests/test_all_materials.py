from SolidProps import SolidProps


def main():
    materials = ['AL5083', 'AL6061', 'ALUMINUM', 'BRASS', 'CARBON_FIBER_NORMAL', 'CARBON_FIBER_PARALLEL',
                 'COPPER', 'COPPER-NICKEL_57-43', 'COPPER-NICKEL_70-30', 'COPPER-NICKEL_90-10',
                 'EPOXY', 'G10_NORMAL_TO_CLOTH' , 'G10_PARALLEL_TO_FILL', 'G10_PARALLEL_TO_WRAP',
                 'GOLD', 'INVAR', 'LEAD', 'KAPTON', 'SAPPHIRE', 'SS304L', 'SS310L', 'TITANIUM']

    T = 150.798
    print(f'T = {T} K\n')

    for material in materials:
        SP = SolidProps(material)
        print(f'{material}')
        print(f'molar density                 : {SP.get_rhomass():.2f} kg/m^3')
        print(f'thermal conductivity          : {SP.get_K(T):.2f} W/(m.K)')
        print(f'specific heat                 : {SP.get_cp(T):.2f} kg/m^3')
        print(f'thermal expansion coefficient : {SP.get_thermal_expansion_coefficient(T):.2e} 1/K')
        print(f'thermal diffusivity           : {SP.get_thermal_diffusivity(T):.2e} m^2/s')
        print(f'electrical resistivity        : {SP.get_electrical_resistivity(T):.2e} ohm.m\n')


if __name__ == "__main__":
    main()