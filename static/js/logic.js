
// Creating map object
var myMap = L.map("map", {
  center: [39.09, -75.69],
  zoom: 4
});

// Adding tile layer to the map
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/light-v10",
  accessToken: "pk.eyJ1IjoiYXJ1bmthcmEiLCJhIjoiY2tmZWppeTM5MDVpazJzbm5saTd5dGR0eiJ9.iLOl6ZYIpPJDOtwDQTk5tg"
}).addTo(myMap);

var investorsData = "static/js/investors2.csv"
//Grab the data with d3
d3.csv(investorsData, function (data) {
console.log(data);


  var investorMarkers = []
  //marker styling
  options = {
    icon: "usd",
    iconShape: "marker",
    borderColor: "#46095E",
    textColor: "#580069",
    backgroundColor: "#B9A3C0"
  };
  //console.log(options);
  //Loop through data
  //Loop through data
  for (var i = 0; i < data.length; i++) {
    // Set the data location property to a variable
    var location = [data[i].lat, data[i].lon]
    //console.log(location)
    // Check for location property
    if (location) {
      // Add a new marker to the cluster group and bind a pop-up
      investorMarkers.push(
        L.marker([location[0], location[1]], {
          icon: L.BeautifyIcon.icon(options)
        }).bindPopup("<h2>" + data[i].name + "</h2> <hr> <h4> Investor Type: " + data[i].type + "<br> " + data[i].website + "</h4>")
      );
    }
  }
  let investorLayer = L.layerGroup(investorMarkers)
  investorLayer.addTo(myMap);

  var container = L.DomUtil.get("map");
  if (container != null) {
    container._leaflet_id = null;
  }
});
