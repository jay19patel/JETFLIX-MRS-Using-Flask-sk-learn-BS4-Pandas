


// Hero Section Slinding Images card 
const cards = document.querySelectorAll('.card');

cards.forEach(card => {
  const images = card.querySelector('.card-images');
  const leftButton = card.querySelector('.left-button');
  const rightButton = card.querySelector('.right-button');
  let currentPosition = 0;
  
  rightButton.addEventListener('click', () => {
    currentPosition -= 300;
    images.style.transform = `translateX(${currentPosition}px)`;
    if (currentPosition < -600) {
      currentPosition = 0;
      images.style.transform = `translateX(${currentPosition}px)`;
    }
  });
  
  leftButton.addEventListener('click', () => {
    currentPosition += 300;
    images.style.transform = `translateX(${currentPosition}px)`;
    if (currentPosition > 0){
        currentPosition = -600;
        images.style.transform = `translateX(${currentPosition}px)`;
        }
        });
        });
