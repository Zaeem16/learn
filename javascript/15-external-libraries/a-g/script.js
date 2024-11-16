import dayjs from "https://unpkg.com/dayjs@1.11.10/esm/index.js";
import isSatSun from "./date-functions.js"
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
/* moved the isWeekend to the date-functions.js file in 15f*/
console.log(isSatSun(today));

/* 15f */
/* default export isWeekend from the date-functions.js file */


/* 15g */
/* default export isWeekend as isSatSun from the date-functions.js file */


