# WeatherApp
An application for weather analysis; gathering information through API services. It's flexible and easy to use. More features will be added in the future, both - GUI and terminal-based related. The user will have
more control over the components and environment.

Future updates will include:  
- A graphical user interface (GUI)  
- Terminal-based features  
- Greater user control over components and environment
  
## Installation
Clone the repository using git (.clone)
```bash
git clone https://github.com/RuslanVe0a/WeatherApp.git
cd ./WeatherApp
```

## Example usage:
  ```python
    import core.WeatherMain

    if __name__ == "__main__":
        _object = core.WeatherMain.Main()
        _object.set_target(("Bulgaria", "Shumen"))
        _object.activate()
        _object.output_friendly()
  ```
## To set an API key
  Open "./core/configuration/config.json" with any text editor and replace the API key with yours, of course the API service
  may differ also other settings inside the 'config.json' file.
