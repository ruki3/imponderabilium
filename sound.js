document.addEventListener("DOMContentLoaded", function() {
	var test = document.getElementById("autoplay").play();

    if (test !== undefined) {
			var plansza = document.getElementsByClassName("audiostarter");
			plansza[0].addEventListener("click", function() {
				setTimeout(function() {
					plansza[0].classList.add("hider")
				}, 500);
                setTimeout(function() {
					document.body.removeChild(plansza[0]);
				}, 1000);
			});
    }
});
