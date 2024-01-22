def vol_shell(r1, r2):
    PI = 3.14

    # Calculate the volume of the outer sphere
    vol_outer = (4/3) * PI * r1 ** 3

    # Calculate the volume of the inner sphere
    vol_inner = (4/3) * PI * r2 ** 3

    # Calculate the volume of the spherical shell
    vol_shell = vol_outer - vol_inner

    # Round the volume to the nearest hundredths
    vol_shell = round(vol_shell, 2)

    return vol_shell
