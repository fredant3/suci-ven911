function form_errors(errors) {
  $.each(errors, function (key, value) {
    const input = $(`#id_${key}`);
    input.addClass("is-invalid");
    input.next().text(value[0].message);
  });
}

// Validar el formulario por parte del cliente
(function () {
  "use strict";
  const form = document.getElementById("form");

  form.addEventListener(
    "submit",
    function (event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }

      form.classList.add("was-validated");
    },
    false
  );

  const estadoSelect = document.getElementById('id_estado');
  estadoSelect && estadoSelect.addEventListener("change", (event) => cargarMunicipios(event));

  const municipioSelect = document.getElementById('id_municipio');
  municipioSelect && municipioSelect.addEventListener("change", (event) => cargarParroquias(event));

  const parroquiaSelect = document.getElementById('id_parroquia');
  primerOption(municipioSelect)
  primerOption(parroquiaSelect)
})();

function reiniciarOptiones(select) {
  if (select.options.length > 0) {
    for (i = select.options.length-1; i >= 0;i--) {
      select.remove(i);
    }
  }
}

function primerOption(select) {
  reiniciarOptiones(select);

  const option = document.createElement('option');
  option.textContent = "---------";
  select.appendChild(option);
}

function cargarMunicipios(event) {
  const idEstado = event.target.value;
  const municipiosSelect = document.getElementById('id_municipio');
  primerOption(municipiosSelect)
  primerOption(document.getElementById('id_parroquia'));
  if (!idEstado || idEstado == "---------") return;

  data.find(estado => estado.id_estado == idEstado).municipios.forEach(each => {
    const option = document.createElement('option');
    option.value = each.municipio;
    option.textContent = each.municipio;
    municipiosSelect.appendChild(option);
  });
}

function cargarParroquias(event) {
  const idMunicipio = event.target.value;
  const estadoSelect = document.getElementById('id_estado');  
  const parroquiasSelect = document.getElementById('id_parroquia');
  primerOption(parroquiasSelect);  
  if (!idMunicipio || idMunicipio == '---------') return;

  data.find(estado => estado.id_estado == estadoSelect.value)
    .municipios.find(search => search.municipio == idMunicipio)
    .parroquias.forEach(each => {
      const option = document.createElement('option');
      option.value = each;
      option.textContent = each;
      parroquiasSelect.appendChild(option);
    });
}