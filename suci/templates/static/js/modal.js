document.addEventListener('DOMContentLoaded', function () {
  const modal = document.getElementById('modal');
  const btnClose = document.getElementsByClassName('close')[0];

  btnClose.onclick = function () {
    modal.style.visibility = "hidden";
    modal.style.opacity = 0;
    modal.style.display = 'none';
  };

  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.visibility = "hidden";
      modal.style.opacity = 0;
      modal.style.display = 'none';
    }
  };
});