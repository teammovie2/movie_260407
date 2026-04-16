const regions = document.querySelectorAll(".region_list li");
const theaters = document.querySelectorAll(".theater_list li");
const movies = document.querySelectorAll(".movie li");

// 지역 선택
regions.forEach(region => {
  region.addEventListener("click", () => {

    const selected = region.innerText;

    // 지역 active
    regions.forEach(r => r.classList.remove("active"));
    region.classList.add("active");

    // 영화관 필터
    theaters.forEach(t => {
      t.style.display =
        t.dataset.region === selected ? "block" : "none";
    });

  });
});

// 지역에 따른 영화관 선택
theaters.forEach(theater => {
  theater.addEventListener("click", () => {

    // 기존 선택 제거
    theaters.forEach(t => t.classList.remove("selected"));

    // 클릭한 극장 선택
    theater.classList.add("selected");

  });
});

//영화 선택
movies.forEach(movie => {
  movie.addEventListener("click", () => {

    // 기존 선택 제거
    movies.forEach(m => m.classList.remove("selected"));

    // 클릭한 극장 선택
    movie.classList.add("selected");

  });
});


// 영화리스트
const API_KEY = "85a24c607dac1e0d9139a903ee0f509b";

fetch(`https://api.themoviedb.org/3/movie/now_playing?api_key=${API_KEY}&language=ko-KR&region=KR`)
  .then(res => res.json())
  .then(async data => {

    const titleList = document.querySelectorAll(".movie_title");

    // 영화 리스트 반복 (li 개수만큼)
    for (let i = 0; i < titleList.length; i++) {

      const movie = data.results[i];
      if (!movie) break;

      // 🔥 한국 관람등급 가져오기
      const res = await fetch(`https://api.themoviedb.org/3/movie/${movie.id}/release_dates?api_key=${API_KEY}`);
      const dates = await res.json();

      const kr = dates.results.find(r => r.iso_3166_1 === "KR");

      let age = "ALL";

      if (kr && kr.release_dates.length > 0) {
        age = kr.release_dates[0].certification || "ALL";
      }

      let ageClass = "";

      if (age === "19") ageClass = "age-19";
      else if (age === "15") ageClass = "age-15";
      else if (age === "12") ageClass = "age-12";
      else ageClass = "age-all";

      // 값 넣기
      titleList[i].innerHTML = `
        <span class="movie_age ${ageClass}">${age}</span>
        ${movie.title}
      `;
    }
  });


// 날짜 자동생성
const dateList = document.querySelector(".date ul");

const today = new Date();

for (let i = 0; i < 7; i++) {
  const date = new Date();
  date.setDate(today.getDate() + i);

  const day = date.getDate(); // 일
  const week = ["일", "월", "화", "수", "목", "금", "토"][date.getDay()];

  const li = document.createElement("li");

  li.innerHTML = `
    <span class="day">${day}</span>
    <span class="week">${week}</span>
  `;

  // 오늘 기본 선택
  if (i === 0) {
  li.classList.add("selected");
  }

  if (week === "토") li.style.color = "blue";
  if (week === "일") li.style.color = "red";


  dateList.appendChild(li);
}

// 날짜 선택
const dates = document.querySelectorAll(".date li");

dates.forEach(date => {
  date.addEventListener("click", () => {

    // 기존 선택 제거
    dates.forEach(d => d.classList.remove("selected"));

    // 선택
    date.classList.add("selected");

    // 🔥 추가된 부분
    const index = [...dates].indexOf(date);

    let times;

    if (index % 2 === 0) {
      times = generateTimes(8, 24);
    } else {
      times = generateTimes(9, 25);
    }

    renderTimes(times);
  });
});


//시간 선택
function generateTimes(startHour, endHour) {
  const times = [];

  let current = new Date();
  current.setHours(startHour, 0, 0, 0);

  const end = new Date();
  end.setHours(endHour, 0, 0, 0);

  while (current <= end) {
    const h = String(current.getHours()).padStart(2, "0");
    const m = String(current.getMinutes()).padStart(2, "0");

    times.push(`${h}:${m}`);

    current.setMinutes(current.getMinutes() + 150); // 2시간 30분
  }

  return times;
}

function renderTimes(times) {
  const timeList = document.querySelector(".time ul");
  timeList.innerHTML = "";

  times.forEach(time => {
    const li = document.createElement("li");

    const seats = Math.floor(Math.random() * 60);

    li.innerHTML = `
      <button class="time_btn ${seats === 0 ? "disabled" : ""}" ${seats === 0 ? "disabled" : ""}>
        ${time}
        <span class="seat">${seats === 0 ? "매진" : `잔여 ${seats}석`}</span>
      </button>
    `;

    timeList.appendChild(li);
  });
}


const timeListEl = document.querySelector(".time");

timeListEl.addEventListener("click", (e) => {
  const btn = e.target.closest(".time_btn");
  if (!btn) return;

  // 기존 선택 제거
  document.querySelectorAll(".time_btn").forEach(b => {
    b.classList.remove("selected");
  });

  
  // 선택
  btn.classList.add("selected");

  // console.log("선택된 시간:", btn.childNodes[0].textContent.trim());
});

renderTimes(generateTimes(8, 24));


