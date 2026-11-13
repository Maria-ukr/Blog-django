
const swiper = new Swiper('.swiper', {
  loop: true,
  pagination: false,
  navigation: {
    nextEl: '.slider__btn-next',
    prevEl: '.slider__btn-prev',
  },
  breakpoints: {
    768: {
      slidesPerView: 2.2,
      spaceBetween: 16,
    },
    1024: {
      slidesPerView: 3.2,
      spaceBetween: 28,
    },
  },
});