import math
# Speicherbedarf für Videoaufnahmen berechnen.
print("Memory calculator for IP-cameras Video Recordings")

cameras = int(input("How many Cameras: "))
resolution_width = int(input("Resolution in pixel width: "))
resolution_height = int(input("Resolution in pixel height: "))
resolution = resolution_width * resolution_height
color_depth = int(input("Color Depth in Bit: "))
compression_dividend = float(input("Compression dividend: "))
compression_divisor = float(input("Compression divisor: "))
compression = compression_dividend / compression_divisor
framerate = int(input("Framerate Per Second: "))
hours = int(input("Recording length in Hours: "))
days = int(input("Recording in Days: "))
time = days * hours * 3600  # 3600 for seconds
result = cameras * resolution * color_depth * compression * framerate * time / 8
# /8 from bit to byte
print(result, "Byte")


def convi():
    print("Convert Result in ...")
    print("(1) Kibibyte")
    print("(2) Mebibyte")
    print("(3) Gibibyte")
    print("(4) Tebibyte")
    print("(5) Pebibyte")
    print("(6) Exbibyte")
    print("(7) Zebibyte")
    print("(8) Yobibyte")
    print("(q) Exit")


convi()

convert_options = ("1", "2", "3", "4", "5", "6", "7", "8", "q")
for i in convert_options:
    select = input("Choose converting Prafix: ").lower()

    if select == "1":
        KiB = result / (2**10)
        if KiB == 0:
            print(f"{KiB} KiB")
            break
        else:
            print(f"{math.floor(KiB * 10)},{round(KiB % 10)} KiB")
            break

    elif select == "2":
        MiB = result / (2**10 * 2**10)
        if MiB == 0:
            print(f"{MiB} MiB")
            break
        else:
            print(f"{math.floor(MiB * 10)},{round(MiB % 10)} MiB")
            break

    elif select == "3":
        GiB = result / (2**10 * 2**10 * 2**10)
        if GiB == 0:
            print(f"{GiB} GiB")
            break
        else:
            print(f"{math.floor(GiB * 10)},{round(GiB % 10)} GiB")
            break

    elif select == "4":
        TiB = result / (2**10 * 2**10 * 2**10 * 2**10)
        if TiB == 0:
            print(f"{TiB} TiB")
            break
        else:
            print(f"{math.floor(TiB * 10)},{round(TiB % 10)} TiB")
            break

    elif select == "5":
        PiB = result / (2**10 * 2**10 * 2**10 * 2**10 * 2**10)
        if PiB == 0:
            print(f"{PiB} PiB")
            break
        else:
            print(f"{math.floor(PiB * 10)},{round(PiB % 10)} PiB")
            break

    elif select == "6":
        EiB = result / (2**10 * 2**10 * 2**10 * 2**10 * 2**10 * 2**10)
        if EiB == 0:
            print(f"{EiB} EiB")
            break
        else:
            print(f"{math.floor(EiB * 10)},{round(EiB % 10)} EiB")
            break

    elif select == "7":
        ZiB = result / (2**10 * 2**10 * 2**10 * 2**10 * 2**10 * 2**10 * 2**10)
        if ZiB == 0:
            print(f"{ZiB} ZiB")
            break
        else:
            print(f"{math.floor(ZiB * 10)},{round(ZiB % 10)} ZiB")
            break

    elif select == "8":
        YiB = result / (2**10 * 2**10 * 2**10 * 2**10 *
                        2**10 * 2**10 * 2**10 * 2**10)
        if YiB == 0:
            print(f"{YiB} YiB")
            break
        else:
            print(f"{math.floor(YiB * 10)},{round(YiB % 10)} YiB")
            break
    elif select == "q":
        exit()
