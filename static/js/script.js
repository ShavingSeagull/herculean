// Script handling adding and removing of classes for certain viewport sizes
window.onload = addRemoveClass();
window.addEventListener("resize", addRemoveClass);


function addRemoveClass() {
    var windowWidth = $(window).innerWidth();

    (function newsPage() {
        if (windowWidth >= 530) {
            $('#edit-button').addClass('pull-right').css('margin', '0 15px');
            $('#delete-button').addClass('pull-right').css('margin', '0 15px');
        }
        else {
            $('#edit-button').removeClass('pull-right').css('margin', '10px 20px');
            $('#delete-button').removeClass('pull-right').css('margin', '10px 20px');
        }
    })();

    (function cartPicture() {
        if (windowWidth < 540) {
            $('.quantity-form').addClass('col-xs-offset-2');
        }
        else {
            $('.quantity-form').removeClass('col-xs-offset-2');
        }
    })();
}


// Script for the carousel
$('.carousel').carousel({
      interval: 5000
});

// Script for the collapsing list of countries
function countryList() {
    $(".country-list").toggleClass("country-active");
    $("#countries").slideToggle();
}

