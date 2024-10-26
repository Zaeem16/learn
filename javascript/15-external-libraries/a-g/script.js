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
console.log(today.format("dddd"));