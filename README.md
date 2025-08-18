# WeatherApp
An application for weather analysis; gathering information through API services. It's flexible and easy to use. More features will be added in the future, both - GUI and terminal-based related. The user will have
more control over the components and environment.

## Example usage:
  ```
    import core.WeatherMain

    if __name__ == "__main__":
        _object = core.WeatherMain.Main()
        _object.set_target(("Bulgaria", "Shumen"))
        _object.activate()
        _object.output_friendly()
  ```
