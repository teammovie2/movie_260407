const API_KEY = "85a24c607dac1e0d9139a903ee0f509b";

fetch(`https://api.themoviedb.org/3/movie/${movieId}?api_key=${API_KEY}&language=ko-KR`)
  .then(res => res.json())
  .then(movie => {

    return fetch(`https://api.themoviedb.org/3/movie/${movieId}/credits?api_key=${API_KEY}&language=ko-KR`)
      .then(res => res.json())
      .then(credits => ({ movie, credits }));
  })
  .then(({ movie, credits }) => {

    const img = document.querySelector(".inner_left img");
    const title = document.querySelector(".movie_title h4");
    const detail = document.querySelector(".detail_right");
    const story = document.querySelector(".story_content");
    const stillBox = document.querySelector(".still_img");

    const imgSrc = movie.poster_path
      ? `https://image.tmdb.org/t/p/w500${movie.poster_path}`
      : "/static/no-image.png";

    img.src = imgSrc;
    title.textContent = movie.title;

    const genres = movie.genres
      ? movie.genres.map(g => g.name).join(", ")
      : "정보 없음";

    const cast = credits.cast
      ? credits.cast.slice(0, 5).map(actor => actor.name).join(", ")
      : "정보 없음";

    detail.innerHTML = `
      <h5>${movie.release_date || "정보 없음"}</h5>
      <h5>${genres}</h5>
      <h5>${movie.runtime || "정보 없음"}분</h5>
      <h5>${movie.vote_average || "정보 없음"}점</h5>
      <h5>${cast}</h5>
      <h5>${movie.tagline || "정보 없음"}</h5>
    `;

    story.textContent = movie.overview || "줄거리 정보 없음";

    fetch(`https://api.themoviedb.org/3/movie/${movieId}/images?api_key=${API_KEY}`)
    .then(res => res.json())
    .then(data => {

      const stills = data.backdrops.slice(0, 5);

      stillBox.innerHTML = stills.map(img => `
        <img src="https://image.tmdb.org/t/p/w500${img.file_path}" />
      `).join("");

    });
  })
  .catch(err => console.error(err));