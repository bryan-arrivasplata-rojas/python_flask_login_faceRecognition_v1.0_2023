//CORRECTO - PERO SE EJECUTARA EL DE ABAJO PARA SIMULAR CARGA
/*window.addEventListener('load', function () {
    // Oculta el loader una vez que la página esté completamente cargada
    document.querySelector('.loader').style.display = 'none';
    // Muestra el contenido de la aplicación
    document.querySelector('.app').style.display = 'block';
});*/
// Evento load para el contenido de la aplicación
window.addEventListener('load', function () {
    setTimeout(function () {
        // Oculta el loader una vez que la página esté completamente cargada
        document.querySelector('.loader').style.display = 'none';
        // Muestra el contenido de la aplicación
        document.querySelector('.app').style.display = 'block';
    }, 2000);
});
$(document).ready(function() {
    // Al cargar la página, ocultar la sección de video

    // Al hacer clic en el enlace "init_video"
    $(".init_video").click(function() {
        // Ocultar la sección de inicio de sesión
        $(".section_login").hide();
        // Ocultar el enlace "init_video"
        $(this).hide();
        // Mostrar la sección de video
        var videoSection = '<a href="/"><img title="Presionar para detener reconocimiento facial" class="img-fluid recognizer_video" src="/video_feed"></a>' +
                           '<form method="POST" action="/welcome"><button class="btn btn-primary mt-3" type="submit" title="Presionar despues de reconocer facialmente">Iniciar sesión</button></form>';
        $(".section_video").append(videoSection);
    });
});

