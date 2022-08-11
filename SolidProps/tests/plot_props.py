import os
import numpy as np
from SolidProps import SolidProps
import matplotlib as mpl
import matplotlib.pyplot as plt


def main():
    materials = {'ALUMINUM': 'pure Al',
                 'COPPER': 'pure Cu',
                 'GOLD': 'pure Au',
                 'LEAD': 'pure Pb',
                 'TITANIUM': 'pure Ti',
                 'AL5083': 'Al-5083',
                 'AL6061': 'Al-6061',
                 'BRASS': 'Brass',
                 'INVAR': 'Invar-36',
                 'SS304L': 'Stainless Steel 304L',
                 'SS310L': 'Stainless Steel 310L',
                 'COPPER-NICKEL_57-43': 'Cu-Ni (0.57/0.43)',
                 'COPPER-NICKEL_70-30': 'Cu-Ni (0.7/0.3)',
                 'COPPER-NICKEL_90-10': 'Cu-Ni (0.9/0.1)',
                 'CARBON_FIBER_NORMAL': 'Carbon Fiber normal',
                 'CARBON_FIBER_PARALLEL': 'Carbon Fiber parallel',
                 'G10_NORMAL_TO_CLOTH': 'G10 normal to cloth',
                 'G10_PARALLEL_TO_FILL': 'G10 parallel to fill',
                 'G10_PARALLEL_TO_WRAP': 'G10 parallel to wrap',
                 'EPOXY': 'Epoxy',
                 'KAPTON': 'Kapton',
                 'SAPPHIRE': 'Sapphire'}

    fig, axes = plt.subplots(2, 3, figsize=(10.3, 6), sharex=True)
    [ax0, ax1, ax2], [ax3, ax4, ax5] = axes

    T = np.arange(1, 300.5, 0.5)
    for material, label in materials.items():
        sp = SolidProps(material)
        line, = ax0.plot(T, [sp.get_rhomass()]*len(T))
        ax1.plot(T, [sp.get_K(_T) for _T in T],
                 color=line.get_color())
        ax2.plot(T, [sp.get_cp(_T) for _T in T],
                 color=line.get_color())
        ax3.plot(T, [sp.get_thermal_expansion_coefficient(_T) for _T in T],
                 color=line.get_color())
        ax4.plot(T, [sp.get_thermal_diffusivity(_T) for _T in T],
                 color=line.get_color(),
                 label=label)
        ax5.plot(T, [sp.get_electrical_resistivity(_T) for _T in T],
                 color=line.get_color())
    for i in range(len(axes)):
        for j in range(len(axes[i])):
            axes[i, j].set_xlim((0, 300))
    ax0.set_yscale('log')
    ax1.set_yscale('log')
    ax2.set_yscale('log')
    ax3.set_yscale('symlog')
    ax4.set_yscale('symlog')
    ax5.set_yscale('log')

    ax1.set_ylim((1e-2, 1e4))
    ax2.set_ylim((1e-3, 1e3))
    ax3.set_ylim((-1e-7, 1e-4))
    ax4.set_ylim((-1e-2, 1e-2))
    ax5.set_ylim((1e-11, 1e-5))
    
    ax4.set_xlabel(r'$T~/~{\rm K}$')

    ax0.set_ylabel(r'$\rho~/~{\rm kg~m^{-3}}$')
    ax1.set_ylabel(r'$k~/~{\rm W~(m~K)^{-1}}$')
    ax2.set_ylabel(r'$c_{\rm p}~/~{\rm J~(kg~K)^{-1}}$')
    ax3.set_ylabel(r'$\alpha~/~{\rm K^{-1}}$')
    ax4.set_ylabel(r'$\alpha_{\rm th}~/~{\rm m^2~s^{-1}}$')
    ax5.set_ylabel(r'$\rho_{\rm el}~/~{\rm \Omega~m}$')

    ax4.set_yticks([-1e-2, 0, 1e-2])

    legend = fig.legend(loc='lower center', ncol=4)
    frame = legend.get_frame()
    frame.set_facecolor('white')
    frame.set_edgecolor('black')
    
    fig.tight_layout(pad=0.2)
    fig.subplots_adjust(bottom=0.41)
    fig.savefig(os.path.join('..','figs','all_props_plot.png'), dpi=600)
    plt.show()


if __name__ == "__main__":
    mpl.rcParams.update({"font.size": 16,
                         "axes.labelsize": 16,
                         "axes.titlesize" : 16,
                         "legend.fontsize": 14,
                         "xtick.top": True,
                         "xtick.bottom": True,
                         "ytick.left": True,
                         "ytick.right": True,
                         "xtick.direction": "in",
                         "ytick.direction": "in"})
    main()