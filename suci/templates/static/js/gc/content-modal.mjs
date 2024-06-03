import { postForm, putForm } from '../modal.mjs'

document.addEventListener('DOMContentLoaded', function () {
  postForm({ textContent: 'Registrar una Red Social', action: 'social-media-account' });
});

document.querySelectorAll('.btn-update').forEach(function (btn) {
  btn.onclick = function (event) {
    event.preventDefault();

    const socialMediaId = btn.getAttribute('data-gc-sma-id');
    putForm({ textContent: 'Actualizar una Red Social', action: `social-media-account/${socialMediaId}` });

    const socialMedia = btn.getAttribute('data-gc-sma');
    document.getElementById('gc-sma-platform').value = socialMedia.platform;
    document.getElementById('gc-sma-username').value = socialMedia.username;
    document.getElementById('gc-sma-url').value = socialMedia.url;
    document.getElementById('gc-sma-followers').value = socialMedia.followers;
    document.getElementById('gc-sma-responsible').value = socialMedia.responsible;
    document.getElementById('gc-sma-publications').value = socialMedia.publications;
  };
});
