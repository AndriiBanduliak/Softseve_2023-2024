const slides = [
    '<img class="carousel-image" src="img/partner1.png" alt="Image 1">',
    '<img class="carousel-image" src="img/partner2.png" alt="Image 2" >',
    '<img class="carousel-image" src="img/partner3.png" alt="Image 3">',
    '<img class="carousel-image" src="img/partner4.png" alt="Image 4">'
  ];
  
  let currentIdx = 0;
  
  function renderSlide() {
      const slideContainer = document.querySelector('.carousel-container .carousel');
      slideContainer.innerHTML = slides[currentIdx];
      if (window.matchMedia('(min-width: 768px)').matches) {
          const secondSlideIdx = currentIdx + 1 >= slides.length ? 0 : currentIdx + 1;
          slideContainer.innerHTML += slides[secondSlideIdx];
          if (window.matchMedia('(min-width: 980px)').matches) {
              const thirdSlideIdx = secondSlideIdx + 1 >= slides.length ? 0 : secondSlideIdx + 1;
              slideContainer.innerHTML += slides[thirdSlideIdx];
          }
      }
  }
  
  renderSlide();
  
  function nextSlide() {
      currentIdx = currentIdx + 1 >= slides.length ? 0 : currentIdx + 1;
      renderSlide();
  }
  
  function prevSlide() {
      currentIdx = currentIdx - 1 <  0 ? slides.length - 1 : currentIdx - 1;
      renderSlide();
  }
  
  // setInterval(nextSlide, 3000);
  
  const btnNext = document.querySelector('.arrow-button.left-arrow');
  btnNext.addEventListener('click', nextSlide);
  
  const btnPrev = document.querySelector('.arrow-button.right-arrow');
  btnPrev.addEventListener('click', prevSlide);
  
  window.addEventListener('resize', renderSlide);