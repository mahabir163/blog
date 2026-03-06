document.addEventListener("DOMContentLoaded", function () {

    const slides = document.querySelectorAll(".slide");
    let index = 0;

    setInterval(() => {

        slides[index].style.opacity = "0";

        index++;

        if (index >= slides.length) {
            index = 0;
        }

        slides[index].style.opacity = "1";

    }, 4000);

});