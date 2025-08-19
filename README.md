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

<img width="591" height="533" alt="image" src="https://github.com/user-attachments/assets/37b01fe5-0cb3-464b-99cf-ecead875d0b2" />

## Example usage using arguments:
  ```bash
  python sample_argument_interface.py -v -q=Shumen | python sample_argument_interface -q=Shumen
  ```
<img width="987" height="549" alt="image" src="https://github.com/user-attachments/assets/078f6080-7c3f-4326-9ea6-f16b86a3a6ac" />

## Example output:
  ```
  * City: Shumen;
  * Region: Shumen;
  * Country: Bulgaria;
  * Latitude: 43.2767;
  * Longitude: 26.9292;
  * Temperature: 22.1;
  * Humidity: 69;
  * Wind: 6.1;
```
## To set an API key
  Open "./core/configuration/config.json" with any text editor and replace the API key with yours, of course the API service
  may differ also other settings inside the 'config.json' file.
