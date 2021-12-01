import { input } from "./input.mjs";
// const input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263];

let counter = 0;
input.forEach((current, i) => {
  const previous = input[i - 1];
  if (!previous) return;

  counter += previous < current ? 1 : 0;
});

console.log("Result 1: ", counter);

const slidingWindows = [];
for (let i = 0; i <= input.length - 3; i++) {
  const slice = input.slice(i, i + 3);
  const sliceSum = slice.reduce((acc, number) => acc + number, 0);
  slidingWindows.push(sliceSum);
}

let counter2 = 0;
slidingWindows.forEach((current, i) => {
  const previous = slidingWindows[i - 1];
  if (!slidingWindows) return;

  counter2 += previous < current ? 1 : 0;
});

console.log("Result 2: ", counter2);
