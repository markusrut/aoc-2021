import { input } from "./input.mjs";
// const input = [
//   "forward 5",
//   "down 5",
//   "forward 8",
//   "up 3",
//   "down 8",
//   "forward 2",
// ];

const mappedInput = input.map((s) => s.split(" "));
console.log(mappedInput);

//Part 1
calcFirst();

function calcFirst() {
  let horizontal = 0,
    depth = 0;
  mappedInput.forEach((movement) => {
    const direction = movement[0];
    const val = Number.parseInt(movement[1]);
    if (direction === "forward") horizontal += val;
    else if (direction === "down") depth += val;
    else if (direction === "up") depth -= val;
  });

  console.log(horizontal * depth);
}

//Part 2
clacSecond();

function clacSecond() {
  let horizontal = 0,
    depth = 0,
    aim = 0;
  mappedInput.forEach((movement) => {
    const direction = movement[0];
    const val = Number.parseInt(movement[1]);
    if (direction === "forward") {
      horizontal += val;
      depth += aim * val;
    } else if (direction === "down") aim += val;
    else if (direction === "up") aim -= val;
  });

  console.log(horizontal * depth);
}
