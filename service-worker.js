self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open('cache').then(function(cache) {
      return cache.addAll([
        '/',
        '/index.html',
        '/assets/icon.png',
        '/assets/Predios.jpg',
        '/assets/settingsIcon2.png',
        '/assets/github.png',
        '/style.css',
        '/bootstrap.min.css',
        '/bootstrap.bundle.min.js'
        // Adicione mais arquivos que você deseja que sejam armazenados em cache aqui
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});
