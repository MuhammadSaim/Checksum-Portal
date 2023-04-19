const mix = require('laravel-mix')


mix.options({
    fileLoaderDirs: {
        fonts: 'assets/fonts',
        images: 'assets/images'
    }
});

mix.js('./src/js/app.js', 'assets/js')
    .sass('./src/scss/app.scss', 'assets/css');


mix.disableNotifications();