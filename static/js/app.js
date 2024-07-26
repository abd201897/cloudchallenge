document.addEventListener('DOMContentLoaded', function() {
    var map = L.map('map').setView([51.5074, -0.1278], 6); // London coordinates and zoom level

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    map.on('click', function(e) {
        var lat = e.latlng.lat;
        var lon = e.latlng.lng;
        fetchWeather(lat, lon);
    });

    function fetchWeather(lat, lon) {
        $.ajax({
            url: `/weather/?lat=${lat}&lon=${lon}`,
            method: 'GET',
            success: function(response) {
                var cityName = response.name;
                var temperature = response.main.temp;
                var description = response.weather[0].description;

                var popupContent = `<b>${cityName}</b><br>Temperature: ${temperature}°C<br>Description: ${description}`;

                L.popup()
                    .setLatLng([lat, lon])
                    .setContent(popupContent)
                    .openOn(map);
            },
            error: function(xhr, status, error) {
                console.error('Error fetching weather data:', error);
                alert('Error fetching weather data. Please try again later.');
            }
        });
    }
});