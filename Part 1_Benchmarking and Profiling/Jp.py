import cProfile
import time

# Attempt to import the profile decorator from line_profiler if installed
try:
    from line_profiler import profile
except ImportError:
    def profile(func):
        """ Dummy decorator in case line_profiler is not installed. """
        return func

# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

@profile
def calculate_z_serial_purepython(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output

@profile
def calc_pure_python(draw_output, desired_width, max_iterations):
    """Create a list of complex coordinates (zs) and complex parameters (cs), build Julia set and display"""
    x_step = (x2 - x1) / desired_width
    y_step = (y2 - y1) / desired_width
    x = [x1 + i * x_step for i in range(desired_width)]
    y = [y1 + i * y_step for i in range(desired_width)]
    zs = [complex(x[i % desired_width], y[i // desired_width]) for i in range(desired_width ** 2)]
    cs = [complex(c_real, c_imag) for i in range(desired_width ** 2)]

    print("Length of x:", len(x))
    print("Total elements:", len(zs))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__ + " took", secs, "seconds")

    assert sum(output) == 33219980  # this sum is expected for a 1000^2 grid with 300 iterations

if __name__ == "__main__":
    cProfile.run('calc_pure_python(draw_output=False, desired_width=1000, max_iterations=300)', 'profile_stats')