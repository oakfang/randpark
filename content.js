const urlsResource = (async () => {
  const episodeListUrl = chrome.extension.getURL("urls");
  const resp = await fetch(episodeListUrl);
  const raw = await resp.text();
  const urls = raw.split("\n").filter(Boolean);
  return urls;
})();

async function goToRandomEpisode() {
  const urls = await urlsResource;
  const randNumber = Math.floor(Math.random() * urls.length);
  const url = urls[randNumber];
  window.location.href = url;
}

for (let randomLink of document.querySelectorAll('a[href="/random-episode"]')) {
  randomLink.href = "#";
  randomLink.addEventListener(
    "click",
    (event) => {
      event.preventDefault();
      event.stopPropagation();
      goToRandomEpisode();
    },
    { capture: true }
  );
}
