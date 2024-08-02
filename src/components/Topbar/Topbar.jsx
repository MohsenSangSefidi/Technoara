import React from "react";

export default function Topbar() {
  return (
    <header className="mt-8 px-4 w-full text-center shadow-lg">
      {/* Topbar */}
      <div className="flex pb-8 items-center justify-between border-[#eeeff4] border-b-2 ">
        <div className="flex items-center justify-between w-[45%]">
          <div className="w-[15%]">
            <div className="font-Dorna text-[1.8rem]">
              <span>تکنو</span>
              <span className="text-primary">آرا</span>
            </div>
          </div>
          <div className="w-[75%]">
            <input
              type="text"
              placeholder="جستجوی محصول و برند محصول ..."
              className="p-3 font-YekanBakh font-bold text-secondary w-full bg-[#F3F5F8]"
            />
          </div>
        </div>
        <div className="flex items-center justify-center gap-4 w-[19rem]">
          <button className="w-[45%] font-YekanBakh bg-white rounded-lg shadow-lg p-3">
            ورود/ ثبت نام
          </button>
          <button className="w-[45%] font-YekanBakh bg-primary shadow-md shadow-primary text-white rounded-md p-3">
            سبد خرید
            0 
          </button>
        </div>
      </div>
      {/* Navbar */}
      <div className="flex items-center mt-5 p-3 pb-4 justify-between">
        <nav className="w-[55%]">
          <ul className="*:font-YekanBakh *:text-secondary *:font-semibold *:p-2 flex items-center justify-between">
            <li className="border-l-2 flex pl-5 cursor-pointer items-center justify-between w-[22%]"> 
            <svg fill="#021959" width="25px" height="25px" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M13,4 L13,11 L20,11 L20,4 L13,4 Z M11,4 L4,4 L4,11 L11,11 L11,4 Z M13,20 L20,20 L20,13 L13,13 L13,20 Z M11,20 L11,13 L4,13 L4,20 L11,20 Z M4,2 L20,2 C21.1045695,2 22,2.8954305 22,4 L22,20 C22,21.1045695 21.1045695,22 20,22 L4,22 C2.8954305,22 2,21.1045695 2,20 L2,4 C2,2.8954305 2.8954305,2 4,2 Z"/>
            </svg>
            <p>دسته بندی محصولات</p>
            </li>
            <li>صفحه اصلی</li>
            <li>فروشگاه</li>
            <li>صفحه محصول</li>
            <li>وبلاگ</li>
            <li>سوالات متداول</li>
            <li>تماس با ما</li>
            <li>درباره ما</li>
          </ul>
        </nav>
          <div>
            <h3 className="font-Dorna text-primary text-[1.1rem] font-bold">شگفت انگیز شو</h3>
          </div>
      </div>
    </header>
  );
}
