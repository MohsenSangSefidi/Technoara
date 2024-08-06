import React from "react";
import TitleBox from "../../components/TitleBox/TitleBox";
import PopularCategoryBox from "./PopularCategoryBox/PopularCategoryBox";
import { Swiper, SwiperSlide } from "swiper/react";
import { useSwiper } from "swiper/react";
import { Navigation } from "swiper/modules";

import "swiper/css";
import 'swiper/css/navigation';

export default function PopularCategory() {

  const swiper = useSwiper();

  return (
    <>
      <TitleBox title={"دسته بندی های محبوب"} link={"مشاهده همه"} />
      <div className="flex items-center justify-between relative mt-12 w-[90%] mx-auto">
        <Swiper
          direction="horizontal"
          modules={[Navigation]}
          navigation={{
            nextEl : ".swiper-button-next",
            prevEl : ".swiper-button-prev"
          }}
          slidesPerView={9}
        >
          <SwiperSlide>
            <PopularCategoryBox />
          </SwiperSlide>
          <SwiperSlide>
            <PopularCategoryBox />
          </SwiperSlide>
          <SwiperSlide>
            <PopularCategoryBox />
          </SwiperSlide>
          <SwiperSlide>
            <PopularCategoryBox />
          </SwiperSlide>
          <SwiperSlide>
            <PopularCategoryBox />
          </SwiperSlide>
          <SwiperSlide>
            <PopularCategoryBox />
          </SwiperSlide>
          <SwiperSlide>
            <PopularCategoryBox />
          </SwiperSlide>
          <SwiperSlide>
            <PopularCategoryBox />
          </SwiperSlide>
          <SwiperSlide>
            <PopularCategoryBox />
          </SwiperSlide>
          <SwiperSlide>
            <PopularCategoryBox />
          </SwiperSlide>
          <SwiperSlide>
            <PopularCategoryBox />
          </SwiperSlide>
          <SwiperSlide>
            <PopularCategoryBox />
          </SwiperSlide>
          <button onClick={() => swiper.slideNext()} className="swiper-button-next">next</button>
          <button onClick={() => swiper.slidePrev()} className="swiper-button-prev">pre</button>
        </Swiper>
      </div>
    </>
  );
}
