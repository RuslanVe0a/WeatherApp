import core.WeatherMain


if __name__ == "__main__":
    _object = core.WeatherMain.Main()
    _object.set_target(("Bulgaria", "Shumen"))
    _object.activate()
    _object.output_friendly()
    print("Test")