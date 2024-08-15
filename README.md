---
title: Technoara
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.23"

---

# Technoara

Base URLs:

* <a href="https://technoara.pythonanywhere.com">Developing: https://technoara.pythonanywhere.com</a>

# Share Docs

* <a href="https://www.apidog.com/apidoc/shared-36366c9a-7598-453f-9225-e51f5024ebc0">For better experience check docs here: https://www.apidog.com/apidoc/shared-36366c9a-7598-453f-9225-e51f5024ebc0</a>

# Product

## GET Filter Product

GET /product/filter-product/

> Body Parameters

```json
{
  "product_title": "string",
  "category_filter": "string",
  "price_filter_start": 0,
  "price_filter_end": 0
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|page|query|string| no |Page Number|
|Authorization|header|string| yes |Token Authorization|
|body|body|object| no |none|
|» product_title|body|string| no |Product title to filter by product name|
|» category_filter|body|string| no |Sub category slug to filter by Sub category|
|» price_filter_start|body|integer| no |Starting price to filter by price|
|» price_filter_end|body|integer| no |Ending price to filter by price|

> Response Examples

> Success

```json
{
  "count": 10,
  "next": "link",
  "previous": "link",
  "results": [
    {
      "id": 1,
      "product_title": "lorem ipsum",
      "product_description": "lorem ipsum",
      "product_price": 1,
      "product_sale_count": 1,
      "product_create_date": "2024-01-01T24:00:00Z",
      "product_slug": "lorem ipsum",
      "product_sub_category": {
        "sub_category_id": 1,
        "sub_category_title": "lorem ipsum",
        "sub_category_slug": "lorem ipsum"
      },
      "product_category": {
        "category_id": 1,
        "category_title": "lorem ipsum",
        "category_slug": "lorem ipsum"
      },
      "product_discount": 1,
      "product_discount_date": "2024-01-01T24:00:00Z",
      "product_cover_url": "http://technoara/uploads/image.jpg"
    },
    {
      "id": 2,
      "product_title": "lorem ipsum",
      "product_description": "lorem ipsum",
      "product_price": 1,
      "product_sale_count": 1,
      "product_create_date": "2024-01-01T24:00:00Z",
      "product_slug": "lorem ipsum",
      "product_sub_category": {
        "sub_category_id": 1,
        "sub_category_title": "lorem ipsum",
        "sub_category_slug": "lorem ipsum"
      },
      "product_category": {
        "category_id": 1,
        "category_title": "lorem ipsum",
        "category_slug": "lorem ipsum"
      },
      "product_discount": 1,
      "product_discount_date": "2024-01-01T24:00:00Z",
      "product_cover_url": "http://technoara/uploads/image.jpg"
    },
    {
      "id": 3,
      "product_title": "lorem ipsum",
      "product_description": "lorem ipsum",
      "product_price": 1,
      "product_sale_count": 1,
      "product_create_date": "2024-01-01T24:00:00Z",
      "product_slug": "lorem ipsum",
      "product_sub_category": {
        "sub_category_id": 1,
        "sub_category_title": "lorem ipsum",
        "sub_category_slug": "lorem ipsum"
      },
      "product_category": {
        "category_id": 1,
        "category_title": "lorem ipsum",
        "category_slug": "lorem ipsum"
      },
      "product_discount": 1,
      "product_discount_date": "2024-01-01T24:00:00Z",
      "product_cover_url": "http://technoara/uploads/image.jpg"
    }
  ]
}
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» count|integer|true|none||Number of products found|
|» next|string¦null|true|none||Next page url|
|» previous|string¦null|true|none||Previous page url|
|» results|[object]|true|none||Results|
|»» id|integer|true|none||Product ID|
|»» product_title|string|true|none||Product title|
|»» product_description|string|true|none||Product description|
|»» product_price|integer|true|none||Product price|
|»» product_sale_count|integer|true|none||Number of product sales|
|»» product_create_date|string|true|none||Product creation date|
|»» product_slug|string|true|none||Product slug|
|»» product_sub_category|object|true|none||Sub category details|
|»»» sub_category_id|integer|true|none||Sub category ID|
|»»» sub_category_title|string|true|none||Sub category title|
|»»» sub_category_slug|string|true|none||Sub category slug|
|»» product_category|object|true|none||Category detail|
|»»» category_id|integer|true|none||Category ID|
|»»» category_title|string|true|none||Category title|
|»»» category_slug|string|true|none||Category slug|
|»» product_discount|integer|true|none||Product discount percentage|
|»» product_discount_date|string¦null|true|none||Product discount end date|
|»» product_discount_price|integer|true|none||Discounted product price|
|»» product_cover_url|string|true|none||Product image URL|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## GET Get Product

GET /product/get-product/{slug}/

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|slug|path|string| yes |none|
|Authorization|header|string| yes |Token Authorization|

> Response Examples

> Success

```json
{
  "id": 1,
  "product_title": "lorem ipsum",
  "product_description": "lorem ipsum",
  "product_price": 1,
  "product_sale_count": 1,
  "product_create_date": "2024-01-01T24:00:00Z",
  "product_slug": "lorem ipsum",
  "product_discount": 1,
  "product_discount_price": 1,
  "product_discount_date": "2024-01-01T24:00:00Z",
  "product_comment_count": 1,
  "product_rating": 1,
  "product_cover_url": "http://technoara/uploads/image.jpg",
  "product_sub_category": {
    "sub_category_id": 1,
    "sub_category_title": "lorem ipsum",
    "sub_category_slug": "lorem ipsum"
  },
  "product_category": {
    "category_id": 1,
    "category_title": "lorem ipsum",
    "category_slug": "lorem ipsum"
  },
  "product_images": [
    {
      "product_image_id": 1,
      "product_image_url": "http://technoara/uploads/image.jpg"
    },
    {
      "product_image_id": 2,
      "product_image_url": "http://technoara/uploads/image.jpg"
    }
  ],
  "product_feature": [
    {
      "feature_title": "lorem ipsum",
      "featuer_description": "lorem ipsum"
    },
    {
      "feature_title": "lorem ipsum",
      "featuer_description": "lorem ipsum"
    }
  ]
}
```

```json
{
  "detail": "اطلاعات برای اعتبارسنجی ارسال نشده است"
}
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

> Record not found

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Record not found|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||Product ID|
|» product_title|string|true|none||Product title|
|» product_description|string|true|none||Product description|
|» product_price|integer|true|none||Product price|
|» product_sale_count|integer|true|none||Number of product sales|
|» product_create_date|string|true|none||Product creation date|
|» product_slug|string|true|none||Product slug|
|» product_discount|integer|true|none||Product discount precentage|
|» product_discount_price|integer|true|none||Discounted product price|
|» product_discount_date|string¦null|true|none||Product discount end date|
|» product_comment_count|integer|true|none||Product comment count|
|» product_rating|number|true|none||Product rating|
|» product_cover_url|string|true|none||Product cover URL|
|» product_sub_category|object|true|none||Sub category detail|
|»» sub_category_id|integer|true|none||Sub category ID|
|»» sub_category_title|string|true|none||Sub category title|
|»» sub_category_slug|string|true|none||Sub category slug|
|» product_category|object|true|none||Category detail|
|»» category_id|integer|true|none||Category ID|
|»» category_title|string|true|none||Category Title|
|»» category_slug|string|true|none||Category Slug|
|» product_images|[object]|true|none||Product images|
|»» product_image_id|integer|true|none||Image ID|
|»» product_image_url|string|true|none||Image URL|
|» product_feature|[object]|true|none||none|
|»» feature_title|string|true|none||Feature title|
|»» featuer_description|string|true|none||Feature description|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

HTTP Status Code **404**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## POST Create Product

POST /product/create-product/

> Body Parameters

```yaml
product_cover: ""
product_title: ""
product_description: ""
product_price: 0
product_category: 0
product_discount: 0
product_discount_date: ""

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |Token Authorization|
|body|body|object| no |none|
|» product_cover|body|string(binary)| yes |Product cover|
|» product_title|body|string| yes |Prodcut title|
|» product_description|body|string| yes |Product description|
|» product_price|body|integer| yes |Product price|
|» product_category|body|integer| yes |Product category ID|
|» product_discount|body|integer| yes |Product discount precentage|
|» product_discount_date|body|string| yes |Product discount end date|

> Response Examples

> Created

```json
{
  "id": 1,
  "product_title": "lorem ipsum",
  "product_description": "lorem ipsum",
  "product_price": 1,
  "product_sale_count": 1,
  "product_create_date": "2024-01-01T24:00:00Z",
  "product_slug": "lorem ipsum",
  "product_discount": 1,
  "product_discount_price": 1,
  "product_discount_date": "2024-01-01T24:00:00Z",
  "product_comment_count": 1,
  "product_rating": 1,
  "product_cover_url": "http://technoara/uploads/image.jpg",
  "product_sub_category": {
    "sub_category_id": 1,
    "sub_category_title": "lorem ipsum",
    "sub_category_slug": "lorem ipsum"
  },
  "product_category": {
    "category_id": 1,
    "category_title": "lorem ipsum",
    "category_slug": "lorem ipsum"
  },
  "product_images": [
    {
      "product_image_id": 1,
      "product_image_url": "http://technoara/uploads/image.jpg"
    },
    {
      "product_image_id": 2,
      "product_image_url": "http://technoara/uploads/image.jpg"
    }
  ],
  "product_feature": [
    {
      "feature_title": "lorem ipsum",
      "featuer_description": "lorem ipsum"
    },
    {
      "feature_title": "lorem ipsum",
      "featuer_description": "lorem ipsum"
    }
  ]
}
```

> Bad Request

```json
{
  "detial": "lorem ipsum",
  "product_title": [
    "lorem ipsum"
  ],
  "product_description": [
    "lorem ipsum"
  ],
  "product_price": [
    "lorem ipsum"
  ],
  "product_category": [
    "lorem ipsum"
  ]
}
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|

### Responses Data Schema

HTTP Status Code **201**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||Product ID|
|» product_title|string|true|none||Product title|
|» product_description|string|true|none||Product description|
|» product_price|integer|true|none||Product price|
|» product_sale_count|integer|true|none||Number of product sales|
|» product_create_date|string|true|none||Product creation date|
|» product_slug|string|true|none||Product slug|
|» product_discount|integer|true|none||Product discount precentage|
|» product_discount_price|integer|true|none||Discounted product price|
|» product_discount_date|string¦null|true|none||Product discount end date|
|» product_comment_count|integer|true|none||Product comment count|
|» product_rating|number|true|none||Product rating|
|» product_cover_url|string|true|none||Product cover URL|
|» product_sub_category|object|true|none||Sub category detail|
|»» sub_category_id|integer|true|none||Sub category ID|
|»» sub_category_title|string|true|none||Sub category title|
|»» sub_category_slug|string|true|none||Sub category slug|
|» product_category|object|true|none||Category detail|
|»» category_id|integer|true|none||Category ID|
|»» category_title|string|true|none||Category title|
|»» category_slug|string|true|none||Category slug|
|» product_images|[object]|true|none||Product images|
|»» product_image_id|integer|true|none||Image ID|
|»» product_image_url|string|true|none||Image URL|
|» product_feature|[object]|true|none||Feature detial|
|»» feature_title|string|true|none||Feature title|
|»» featuer_description|string|true|none||Feature description|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detial|string|false|none||Error text|
|» product_title|[string]|false|none||none|
|» product_description|[string]|false|none||none|
|» product_price|[string]|false|none||none|
|» product_category|[string]|false|none||none|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## POST Create Comment

POST /product/create-comment/

> Body Parameters

```json
{
  "comment_text": "string",
  "comment_rating": 0,
  "comment_product": 0,
  "comment_user": 0
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |Token Authorization|
|body|body|object| no |none|
|» comment_text|body|string| yes |Comment text|
|» comment_rating|body|integer| yes |Comment rating|
|» comment_product|body|integer| yes |The ID of the product that the comment is for|
|» comment_user|body|integer| yes |The ID of the user that the comment is for|

> Response Examples

> Created

```json
{
  "id": 1,
  "comment_text": "lorem ipsum",
  "comment_rating": 1,
  "comment_create_date": "2024-01-01T24:00:00Z",
  "comment_product": {
    "product_id": 1,
    "product_title": "lorem ipsum",
    "product_slug": "lorem ipsum"
  },
  "comment_user": {
    "user_id": 1,
    "user_name": "lorem ipsum",
    "user_email": "loremipsum@gmail.com"
  }
}
```

> Bad Request

```json
{
  "detail": "lorem ipsum",
  "comment_text": [
    "lorem ipsum"
  ],
  "comment_rating": [
    "lorem ipsum"
  ],
  "comment_product": [
    "lorem ipsum"
  ],
  "comment_user": [
    "lorem ipsum"
  ]
}
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|

### Responses Data Schema

HTTP Status Code **201**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||Comment ID|
|» comment_text|string|true|none||Comment text|
|» comment_rating|integer|true|none||Comment rating|
|» comment_create_date|string|true|none||Comment create date|
|» comment_product|object|true|none||Comment product|
|»» product_id|integer|true|none||Product ID|
|»» product_title|string|true|none||Product title|
|»» product_slug|string|true|none||Product slug|
|» comment_user|object|true|none||Comment user|
|»» user_id|integer|true|none||User ID|
|»» user_name|string|true|none||Username|
|»» user_email|string|true|none||User email|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|false|none||Error text|
|» comment_text|[string]|false|none||none|
|» comment_rating|[string]|false|none||none|
|» comment_product|[string]|false|none||none|
|» comment_user|[string]|false|none||none|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## POST Create Feature

POST /product/create-feature/

> Body Parameters

```json
{
  "feature_title": "string",
  "feature_description": "string",
  "feature_product": 0
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |Token Authorization|
|body|body|object| no |none|
|» feature_title|body|string| yes |Feature title|
|» feature_description|body|string| yes |Feature description|
|» feature_product|body|integer| yes |The ID of the product that has the feature|

> Response Examples

> Created

```json
{
  "id": 1,
  "feature_title": "lorem ipsum",
  "feature_description": "lorem ipsum",
  "feature_product": {
    "product_id": 1,
    "product_title": "lorem ipsum",
    "product_slug": "lorem ipsum"
  }
}
```

> Bad Request

```json
{
  "detail": "lorem ipsum",
  "feature_title": [
    "lorem ipsum"
  ],
  "feature_description": [
    "lorem ipsum"
  ],
  "feature_product": [
    "lorem ipsum"
  ]
}
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|

### Responses Data Schema

HTTP Status Code **201**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||Feature ID|
|» feature_title|string|true|none||Feature title|
|» feature_description|string|true|none||Feature description|
|» feature_product|object|true|none||The product that has the feature|
|»» product_id|integer|true|none||Product ID|
|»» product_title|string|true|none||Product title|
|»» product_slug|string|true|none||Product slug|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|false|none||Error text|
|» feature_title|[string]|false|none||none|
|» feature_description|[string]|false|none||none|
|» feature_product|[string]|false|none||none|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## POST Create Product Image

POST /product/create-images/

> Body Parameters

```yaml
product_img: ""
product: 0

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |Token Authorization|
|body|body|object| no |none|
|» product_img|body|string(binary)| yes |none|
|» product|body|integer| yes |none|

> Response Examples

> Created

```json
{
  "id": 1,
  "product_img_url": "http://technoara/uploads/image.jpg",
  "product_detail": {
    "product_id": 1,
    "product_title": "lorem ipsum",
    "product_slug": "lorem ipsum"
  }
}
```

> Bad Request

```json
{
  "detail": "lorem ipsum",
  "product_img": [
    "lorem ipsum"
  ],
  "product": [
    "lorem ipsum"
  ]
}
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|

### Responses Data Schema

HTTP Status Code **201**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||Image ID|
|» product_img_url|string|true|none||Image url|
|» product_detail|object|true|none||The product that the photo is for|
|»» product_id|integer|true|none||Product ID|
|»» product_title|string|true|none||Product title|
|»» product_slug|string|true|none||Product slug|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|false|none||Error text|
|» product_img|[string]|false|none||none|
|» product|[string]|false|none||none|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## GET Get Category

GET /product/get-category/

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |Token Authorization|

> Response Examples

> Success

```json
[
  {
    "id": 1,
    "category_title": "lorem ipsum",
    "category_slug": "lorem ipsum",
    "sub_categories": [
      {
        "sub_category_id": 1,
        "sub_category_title": "lorem ipsum",
        "sub_category_slug": "lorem ipsum"
      },
      {
        "sub_category_id": 2,
        "sub_category_title": "lorem ipsum",
        "sub_category_slug": "lorem ipsum"
      }
    ]
  }
]
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||Category ID|
|» category_title|string|true|none||Category title|
|» category_slug|string|true|none||Category slug|
|» sub_categories|[object]|true|none||Sub Categories|
|»» sub_category_id|integer|true|none||Sub category ID|
|»» sub_category_title|string|true|none||Sub category title|
|»» sub_category_slug|string|true|none||Sub category slug|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## GET Get Product Comments

GET /product/get-product-comments/{slug}/

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|slug|path|string| yes |none|
|Authorization|header|string| yes |Token Authorization|

> Response Examples

> Success

```json
[
  {
    "id": 1,
    "comment_text": "lorem ipsum",
    "comment_rating": 1,
    "comment_create_date": "2024-08-10T06:00:00Z",
    "comment_product": {
      "product_id": 1,
      "product_title": "lorem ipsum",
      "product_slug": "lorem ipsum"
    },
    "comment_user": {
      "user_id": 1,
      "user_name": "lorem ipsum",
      "user_email": "lorem ipsum@gmail.com"
    }
  },
  {
    "id": 2,
    "comment_text": "lorem ipsum",
    "comment_rating": 2,
    "comment_create_date": "2024-08-10T06:00:00Z",
    "comment_product": {
      "product_id": 2,
      "product_title": "lorem ipsum",
      "product_slug": "lorem ipsum"
    },
    "comment_user": {
      "user_id": 2,
      "user_name": "lorem ipsum",
      "user_email": "lorem ipsum@gmail.com"
    }
  }
]
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» id|integer|true|none||Comment ID|
|» comment_text|string|true|none||Comment text|
|» comment_rating|integer|true|none||Comment rating|
|» comment_create_date|string|true|none||Comment creation date|
|» comment_product|object|true|none||The product that the comment is for|
|»» product_id|integer|true|none||Product ID|
|»» product_title|string|true|none||Product title|
|»» product_slug|string|true|none||Product slug|
|» comment_user|object|true|none||The user that the comment is for|
|»» user_id|integer|true|none||User ID|
|»» user_name|string|true|none||Username|
|»» user_email|string|true|none||Useremail|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

# Users

## POST Create User

POST /users/create-user/

> Body Parameters

```yaml
user_avatar: ""
username: ""
first_name: ""
last_name: ""
email: ""
password: ""

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |Token Authorization|
|body|body|object| no |none|
|» user_avatar|body|string(binary)| no |none|
|» username|body|string| no |none|
|» first_name|body|string| no |none|
|» last_name|body|string| no |none|
|» email|body|string| no |none|
|» password|body|string| no |none|

> Response Examples

> Created

```json
{
  "detail": "lorem ipsum",
  "user-detail": {
    "user_avatar_url": "",
    "username": "lorem ipsum",
    "first_name": "lorem ipsum",
    "last_name": "lorem ipsum",
    "email": "lorem ipsum",
    "user_token": "lorem ipsum",
    "user_verify_code": 123456,
    "last_login": null,
    "user_create_date": "lorem ipsum",
    "is_active": true,
    "is_superuser": false,
    "is_staff": false
  }
}
```

> Bad Request

```json
{
  "detail": "lorem ipsum",
  "username": [
    "lorem ipsum"
  ],
  "email": [
    "lorem ipsum"
  ],
  "password": [
    "lorem ipsum"
  ]
}
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|

### Responses Data Schema

HTTP Status Code **201**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||Send email message|
|» user-detail|object|true|none||User Detail|
|»» user_avatar_url|string|true|none||Avatar URL|
|»» username|string|true|none||Username|
|»» first_name|string|true|none||First name|
|»» last_name|string|true|none||Last name|
|»» email|string|true|none||Email|
|»» user_token|string|true|none||User token|
|»» user_verify_code|integer|true|none||Verify code|
|»» last_login|string¦null|true|none||Last login|
|»» user_create_date|string|true|none||User create date|
|»» is_active|boolean|true|none||Is Active|
|»» is_superuser|boolean|true|none||Is Superuser|
|»» is_staff|boolean|true|none||Is Staff|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|false|none||Message|
|» username|[string]|false|none||Message|
|» email|[string]|false|none||Message|
|» password|[string]|false|none||Message|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## PUT Active User

PUT /users/active-user/

> Body Parameters

```json
{
  "user_token": "string",
  "verify_code": "string"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |Token Authorization|
|body|body|object| no |none|
|» user_token|body|string| yes |none|
|» verify_code|body|string| yes |none|

> Response Examples

> Success

```json
{
  "detail": "lorem ipsum"
}
```

> Bad Request

```json
{
  "detail": "lorem ipsum",
  "user_token": [
    "lorem ipsum"
  ],
  "verify_code": [
    "lorem ipsum"
  ]
}
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||Message|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||Message|
|» user_token|[string]|true|none||Message|
|» verify_code|[string]|true|none||Message|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## POST Login User

POST /users/login-user/

> Body Parameters

```json
{
  "email": "string",
  "password": "string"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |Token Authorization|
|body|body|object| no |none|
|» email|body|string| yes |none|
|» password|body|string| yes |none|

> Response Examples

> OK

```json
{
  "token": "lorem ipsum",
  "user-detail": {
    "user_avatar_url": "http://technoara/uploads/image.jpg",
    "username": "lorem ipsum",
    "first_name": "lorem ipsum",
    "last_name": "lorem ipsum",
    "email": "lorem ipsum",
    "user_token": "lorem ipsum",
    "user_verify_code": 1,
    "last_login": "lorem ipsum",
    "user_create_date": "2024-08-15T10:13:10.096Z",
    "is_active": true,
    "is_superuser": true,
    "is_staff": true
  }
}
```

> Bad Request

```json
{
  "detail": "lorem ipsum",
  "email": [
    "lorem ipsum"
  ],
  "password": [
    "lorem ipsum"
  ]
}
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» token|string|true|none||Login token|
|» user-detail|object|true|none||User detail|
|»» user_avatar_url|string|true|none||Avatar URL|
|»» username|string|true|none||Username|
|»» first_name|string|true|none||First name|
|»» last_name|string|true|none||Last name|
|»» email|string|true|none||Email|
|»» user_token|string|true|none||User token|
|»» user_verify_code|integer|true|none||Verify code|
|»» last_login|null|true|none||Last login|
|»» user_create_date|string|true|none||User create date|
|»» is_active|boolean|true|none||Is Active|
|»» is_superuser|boolean|true|none||Is Superuser|
|»» is_staff|boolean|true|none||Is Staff|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||Message|
|» email|[string]|true|none||Message|
|» password|[string]|true|none||Message|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## GET Get User Detail

GET /users/get-user/{user_token}/

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|user_token|path|string| yes |none|
|Authorization|header|string| yes |Token Authorization|

> Response Examples

> Success

```json
{
  "user_avatar_url": "http://technoara/uploads/image.jpg",
  "username": "lorem ipsum",
  "first_name": "lorem ipsum",
  "last_name": "lorem ipsum",
  "email": "lorem ipsum",
  "user_token": "lorem ipsum",
  "user_verify_code": 1,
  "last_login": "lorem ipsum",
  "user_create_date": "2024-08-14T19:47:58.507Z",
  "is_active": true,
  "is_superuser": true,
  "is_staff": true
}
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

> Record not found

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Record not found|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» user_avatar_url|string|true|none||Avatar URL|
|» username|string|true|none||Username|
|» first_name|string|true|none||First name|
|» last_name|string|true|none||Last name|
|» email|string|true|none||Email|
|» user_token|string|true|none||User token|
|» user_verify_code|integer|true|none||Verify code|
|» last_login|null|true|none||Last login|
|» user_create_date|string|true|none||User create date|
|» is_active|boolean|true|none||Is Active|
|» is_superuser|boolean|true|none||Is Super user|
|» is_staff|boolean|true|none||Is Staff|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

HTTP Status Code **404**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

## POST Send Verify Code

POST /users/send-verify-code/

> Body Parameters

```json
{
  "user_token": "string",
  "email": "string"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string| yes |Token Authorization|
|body|body|object| no |none|
|» user_token|body|string| yes |none|
|» email|body|string| yes |none|

> Response Examples

> Success

```json
{
  "detail": "lorem ipsum"
}
```

```json
{
  "user_token": [
    "This field is required."
  ],
  "email": [
    "This field is required."
  ]
}
```

> Bad Request

```json
{
  "detail": "lorem ipsum",
  "user_token": [
    "lorem ipsum"
  ],
  "email": [
    "lorem ipsum"
  ]
}
```

> Unauthorized

```json
{
  "detail": "lorem ipsum"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||Send Mail Messege|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|false|none||Message|
|» user_token|[string]|false|none||Message|
|» email|[string]|false|none||Message|

HTTP Status Code **401**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» detail|string|true|none||none|

