const translations = {
  zh: {
    navCheckin: "活动签到",
    navPickup: "接机申请",
    platformLabel: "OUR PLATFORM",
    homeTitle: "让学生组织管理\n更高效、更清晰",
    aboutTitle: "关于 UMCSSA Platform",
    aboutText: "UMCSSA Platform 是一个为密西根大学中国学生学者联合会设计的活动管理系统，用于支持新生见面会签到、接机报名、志愿者管理、报销流程与数据统计。平台旨在减少重复人工操作，提高活动组织效率，并为参与者提供更顺畅的体验。",

    eventLabel: "EVENT CHECK-IN",
    eventIndexTitle: "请选择活动\n进入签到界面",
    currentEvents: "当前活动",
    futureEvents: "未来活动",
    beijingEvent: "2026 年新生见面会（北京场）",
    shenzhenEvent: "2026 年新生见面会（深圳场）",
    galaEvent: "2027 年春节迎新晚会",
    openEvent: "开放中",
    closedEvent: "未开放",
    enterBeijing: "点击进入北京场签到界面",
    notOpen: "暂未开放",

    emailLabel: "UM 电子邮箱",
    guestLabel: "实际随行人员数量",
    checkinButton: "签到",
    backToEvents: "← 回到活动列表",
    enterEmail: "请输入您的 UM 电子邮箱。",
    serverError: "服务器连接失败，请联系现场工作人员。",
    welcome: "欢迎参会"
  },

  en: {
    navCheckin: "Event Check-in",
    navPickup: "Airport Pickup",
    platformLabel: "OUR PLATFORM",
    homeTitle: "Making Student Organization Management\nMore Efficient and Clear",
    aboutTitle: "About UMCSSA Platform",
    aboutText: "UMCSSA Platform is an event management system designed for the University of Michigan Chinese Students and Scholars Association. It supports new student meet-and-greet check-in, airport pickup registration, volunteer management, reimbursement workflows, and data statistics. The platform aims to reduce repetitive manual work, improve event operation efficiency, and provide a smoother experience for participants.",

    eventLabel: "EVENT CHECK-IN",
    eventIndexTitle: "Select an Event\nto Continue",
    currentEvents: "Current Events",
    futureEvents: "Future Events",
    beijingEvent: "2026 New Student Meet & Greet (Beijing Session)",
    shenzhenEvent: "2026 New Student Meet & Greet (Shenzhen Session)",
    galaEvent: "2027 Spring Festival Gala",
    openEvent: "Open",
    closedEvent: "Not Open",
    enterBeijing: "Enter Beijing Session Check-in",
    notOpen: "Not available yet",

    emailLabel: "UM Email",
    guestLabel: "Actual Guest Count",
    checkinButton: "Check In",
    backToEvents: "← Back to Event List",
    enterEmail: "Please enter your UM email.",
    serverError: "Server connection failed. Please contact staff.",
    welcome: "Welcome"
  }
};

function getLang() {
  return localStorage.getItem("lang") || "zh";
}

function setLanguage(lang) {
  localStorage.setItem("lang", lang);
  applyLanguage();
}