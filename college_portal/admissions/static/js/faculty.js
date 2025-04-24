document.addEventListener('DOMContentLoaded', function () {
  const toggleButtons = document.querySelectorAll('.toggle-button');
  
  toggleButtons.forEach(button => {
      button.addEventListener('click', function () {
          const parentSection = this.closest('.department-section');
          const facultyGrid = parentSection.querySelector('.faculty-grid');
          
          // Toggle the grid visibility
          facultyGrid.style.display = (facultyGrid.style.display === 'none' || facultyGrid.style.display === '') ? 'grid' : 'none';
          
          // Change the toggle button text
          this.textContent = facultyGrid.style.display === 'none' ? '[+]' : '[-]';
      });
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const facultyCards = document.querySelectorAll('.faculty-card');

  facultyCards.forEach(card => {
      card.addEventListener('click', () => {
          card.classList.toggle('flipped');
      });
  });
});
