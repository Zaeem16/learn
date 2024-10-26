import dayjs from "https://unpkg.com/dayjs@1.11.10/esm/index.js";
const today = dayjs();

/* 15a */
const after5days = today.add(5, "days");
console.log(after5days.format("MMMM D"));

/* 15b */
const after1month = today.add(1, "months");
console.log(after1month.format("MMMM D"));

/* 15c */
const before1month = today.subtract(1, "months");
console.log(before1month.format("MMMM D"));

/* 15d */
const todayDayName = today.format("dddd");
console.log(todayDayName);

/* 15e */ 
function isWeekend(date) {
    const day = dayjs(date).day(); // Get the day of the week (0 = Sunday, 6 = Saturday)
    if (day === 0) {
        return "Sunday";
    }
    else if (day === 6) {
        return "Saturday";
    }
    else {
        return "Weekday";
    }
}

console.log(isWeekend(today));