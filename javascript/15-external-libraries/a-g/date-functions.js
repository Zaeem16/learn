import dayjs from "https://unpkg.com/dayjs@1.11.10/esm/index.js";

export default function isWeekend(date) {
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


