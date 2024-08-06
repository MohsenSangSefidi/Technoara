import Index from "./pages/Index/Index"
import Auth from "./pages/Auth/Auth"
import Basket from "./pages/Basket/Basket"
import Category from "./pages/Category/Category"
import ProductDiscount from "./pages/ProductsDiscount/ProductsDiscount"
import Product from "./pages/Product/Product"
import Articles from "./pages/Articles/Articles"

const routes = [
    { path : "/" , element : <Index /> },
    { path : "/articles" , element : <Articles /> },
    { path : "/auth" , element : <Auth /> },
    { path : "/basket" , element : <Basket /> },
    { path : "/product" , element : <Product /> },
    { path : "/category" , element : <Category /> },
    { path : "/productdiscount" , element : <ProductDiscount /> },
];

export default routes;