import React from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import {Pagination , Autoplay} from "swiper/modules"
import "swiper/css";
import 'swiper/css/pagination';

export default function Banner() {
  return (
    <div className="w-[100%] xs:h-[15rem] sm:h-[20rem] lg:h-[30rem]">
      <Swiper 
        className="h-[100%]"
        spaceBetween={50}
        slidesPerView={1}
        modules={[Pagination , Autoplay]}
        direction="horizontal"
        autoplay={{delay:1500}}
        loop={true}
        pagination={{ clickable: true , bulletClass : "swiper-pagination-bullet" , bulletActiveClass:"swiper-pagination-bullet-active"}}
      >
        <SwiperSlide className="h-[100%]">
          <div className="h-[100%] overflow-hidden rounded-xl">
            <img
              src="../../../public/images/banner/newSlider2-1.jpg"
              className="w-[100%] h-[100%]"
              alt=""
            />
          </div>
        </SwiperSlide>
        <SwiperSlide className="h-[100%]">
          <div className="overflow-hidden h-[100%] rounded-xl">
            <img
              src="../../../public/images/banner/newSlider3-1.jpg"
              className="w-[100%] h-[100%]"
              alt=""
            />
          </div>
        </SwiperSlide>
        <SwiperSlide className="h-[100%]">
          <div className="overflow-hidden h-[100%] rounded-xl">
            <img
              src="../../../public/images/banner/newSlider4-1.jpg"
              className="w-[100%] h-[100%]"
              alt=""
            />
          </div>
        </SwiperSlide>
      </Swiper>
    </div>
  );
}
