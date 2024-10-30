document.querySelector('.welcomeBtn').addEventListener('click', () => {
    document.querySelector('.infoPage').scrollIntoView({behavior: 'smooth'})
})

document.querySelector('#burger').addEventListener('click', () => {
    document.querySelector('.header').classList.toggle('open');
  })