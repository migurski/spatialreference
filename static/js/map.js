function init(code) {
    m = new OpenLayers.Map('map', {'maxResolution': 360/512});
    m.addLayer(new OpenLayers.Layer.WMS('', 'http://labs.metacarta.com/wms-c/Basic.py', {'layers':'basic'}));
    m.addLayer(new OpenLayers.Layer.Markers(''));
    m.zoomToMaxExtent();
    m.marker = new OpenLayers.Marker(new OpenLayers.LonLat(0,0));
    m.layers[1].addMarker(m.marker);
    if (window.bounds) {
    m.addLayer(new OpenLayers.Layer.Boxes());
    m.layers[2].addMarker(new OpenLayers.Marker.Box(bounds));
    }
    m.events.register('moveend', m, function() {
        var c = this.getCenter();
        this.marker.moveTo(this.getLayerPxFromLonLat(c));
        document.getElementById("out").innerHTML = "Waiting...";
        document.getElementById("in").innerHTML = [c.lon,c.lat].join(", ");
        var json = '{"type":"Feature", "geometry":{"type":"Point", "coordinates":[' + c.lon + ', '+ c.lat + ']},"properties":{}}';
        var s = document.createElement("script");
        s.src = "/projection/?json=" + escape(json) + "&inref=EPSG:4326&outref="+code+"&callback=project_out"
        document.body.appendChild(s);
    });
    if (window.bounds) {
        m.setCenter(bounds.getCenterLonLat());
    } else {    
        m.zoomToMaxExtent();
    }    
}    
function project_out(data) {
    if (data.coordinates) {
      document.getElementById("out").innerHTML = data.coordinates.join(", ");
    } else if (data.error) {
        if (window.console) {
            console.log(data.error);
        }
        document.getElementById('out').innerHTML = 'An error occurred.';
    }    
}
