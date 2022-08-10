from SolidProps import SolidProps
import time


def main():
    T = 123.456
    n_iters = 100000
    SP = SolidProps('brass')

    print(f'Calculation time of any property apart from the thermal diffusivity:')
    tic = time.time()
    for i in range(n_iters):
        SP.get_cp(T)
    toc = time.time()
    print(f'Total time elapsed {toc-tic:.3f} sec for {n_iters:.1e} calculations')
    print(f'The average time per calculation is {(toc-tic)/n_iters*1e6:.3f} micro-seconds\n')

    print(f'Calculation time of the thermal diffusivity:')
    tic = time.time()
    for i in range(n_iters):
        SP.get_thermal_diffusivity(T)
    toc = time.time()
    print(f'Total time elapsed {toc-tic:.3f} sec for {n_iters:.1e} calculations')
    print(f'The average time per calculation is {(toc-tic)/n_iters*1e6:.3f} micro-seconds')


if __name__ == "__main__":
    main()