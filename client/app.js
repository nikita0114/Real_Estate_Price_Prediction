function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i = 0; i < uiBathrooms.length; i++) {
        if (uiBathrooms[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1;
}

function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for (var i = 0; i < uiBHK.length; i++) {
        if (uiBHK[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1;
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    // Use the appropriate API URL
    var url = "/api/predict_home_price";

    $.ajax({
        type: "POST",
        url: url,
        data: {
            total_sqft: parseFloat(sqft.value),
            bhk: bhk,
            bath: bathrooms,
            location: location.value
        },
        success: function(data, status) {
            console.log("Prediction received:", data);
            if (data.estimated_price) {
                estPrice.innerHTML = "<h2>Estimated Price: ₹" + data.estimated_price.toString() + " Lakh</h2>";
            } else {
                estPrice.innerHTML = "<h2>Price prediction failed.</h2>";
            }
        },
        error: function(xhr, status, error) {
            console.error("Error during API call:", error);
            estPrice.innerHTML = "<h2>Something went wrong!</h2>";
        }
    });
}

function onPageLoad() {
    console.log("document loaded");

    // URL for the locations API endpoint
    var url = "/api/get_location_names";

    $.get(url, function(data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            var locations = data.locations;
            var uiLocations = $('#uiLocations');
            uiLocations.empty();
            for (var i in locations) {
                var opt = new Option(locations[i], locations[i]);
                uiLocations.append(opt);
            }
        }
    });
}

// Load locations when the page is ready
window.onload = onPageLoad;
