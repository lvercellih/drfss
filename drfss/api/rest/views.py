from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_swagger.renderers import SwaggerUIRenderer


class JSONOpenAPIRenderer(JSONRenderer):
    format = 'openapi'


class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        SwaggerUIRenderer,
        JSONOpenAPIRenderer
    ]

    def get(self, request):
        return Response(schema)

"""
Schema del api de instagram obtenido de http://editor.swagger.io/
"""
schema = {
    "swagger": "2.0",
    "info": {
        "version": "v1",
        "title": "Instagram API",
        "description": "The first version of the Instagram API is an exciting step forward towards\nmaking it easier for users to have open access to their data. We created it\nso that you can surface the amazing content Instagram users share every\nsecond, in fun and innovative ways.\n\nBuild something great!\n\nOnce you've\n[registered your client](http://instagram.com/developer/register/) it's easy\nto start requesting data from Instagram.\n\nAll endpoints are only accessible via https and are located at\n`api.instagram.com`. For instance: you can grab the most popular photos at\nthe moment by accessing the following URL with your client ID\n(replace CLIENT-ID with your own):\n```\n  https://api.instagram.com/v1/media/popular?client_id=CLIENT-ID\n```\nYou're best off using an access_token for the authenticated user for each\nendpoint, though many endpoints don't require it.\nIn some cases an access_token will give you more access to information, and\nin all cases, it means that you are operating under a per-access_token limit\nvs. the same limit for your single client_id.\n\n\n## Limits\nBe nice. If you're sending too many requests too quickly, we'll send back a\n`503` error code (server unavailable).\nYou are limited to 5000 requests per hour per `access_token` or `client_id`\noverall. Practically, this means you should (when possible) authenticate\nusers so that limits are well outside the reach of a given user.\n\n## Deleting Objects\nWe do our best to have all our URLs be\n[RESTful](http://en.wikipedia.org/wiki/Representational_state_transfer).\nEvery endpoint (URL) may support one of four different http verbs. GET\nrequests fetch information about an object, POST requests create objects,\nPUT requests update objects, and finally DELETE requests will delete\nobjects.\n\nSince many old browsers don't support PUT or DELETE, we've made it easy to\nfake PUTs and DELETEs. All you have to do is do a POST with _method=PUT or\n_method=DELETE as a parameter and we will treat it as if you used PUT or\nDELETE respectively.\n\n## Structure\n\n### The Envelope\nEvery response is contained by an envelope. That is, each response has a\npredictable set of keys with which you can expect to interact:\n```json\n{\n    \"meta\": {\n        \"code\": 200\n    },\n    \"data\": {\n        ...\n    },\n    \"pagination\": {\n        \"next_url\": \"...\",\n        \"next_max_id\": \"13872296\"\n    }\n}\n```\n\n#### META\nThe meta key is used to communicate extra information about the response to\nthe developer. If all goes well, you'll only ever see a code key with value\n200. However, sometimes things go wrong, and in that case you might see a\nresponse like:\n```json\n{\n    \"meta\": {\n        \"error_type\": \"OAuthException\",\n        \"code\": 400,\n        \"error_message\": \"...\"\n    }\n}\n```\n\n#### DATA\nThe data key is the meat of the response. It may be a list or dictionary,\nbut either way this is where you'll find the data you requested.\n#### PAGINATION\nSometimes you just can't get enough. For this reason, we've provided a\nconvenient way to access more data in any request for sequential data.\nSimply call the url in the next_url parameter and we'll respond with the\nnext set of data.\n```json\n{\n    ...\n    \"pagination\": {\n        \"next_url\": \"https://api.instagram.com/v1/tags/puppy/media/recent?access_token=fb2e77d.47a0479900504cb3ab4a1f626d174d2d&max_id=13872296\",\n        \"next_max_id\": \"13872296\"\n    }\n}\n```\nOn views where pagination is present, we also support the \"count\" parameter.\nSimply set this to the number of items you'd like to receive. Note that the\ndefault values should be fine for most applications - but if you decide to\nincrease this number there is a maximum value defined on each endpoint.\n\n### JSONP\nIf you're writing an AJAX application, and you'd like to wrap our response\nwith a callback, all you have to do is specify a callback parameter with\nany API call:\n```\nhttps://api.instagram.com/v1/tags/coffee/media/recent?access_token=fb2e77d.47a0479900504cb3ab4a1f626d174d2d&callback=callbackFunction\n```\nWould respond with:\n```js\ncallbackFunction({\n    ...\n});\n```\n",
        "termsOfService": "http://instagram.com/about/legal/terms/api"
    },
    "host": "api.instagram.com",
    "basePath": "/v1",
    "schemes": [
        "https"
    ],
    "produces": [
        "application/json"
    ],
    "consumes": [
        "application/json"
    ],
    "tags": [
        {
            "name": "Users"
        },
        {
            "name": "Relationships",
            "description": "Relationships are expressed using the following terms:\n\n**outgoing_status**: Your relationship to the user. Can be \"follows\",\n  \"requested\", \"none\".\n**incoming_status**: A user's relationship to you. Can be \"followed_by\",\n  \"requested_by\", \"blocked_by_you\", \"none\".\n"
        },
        {
            "name": "Media",
            "description": "At this time, uploading via the API is not possible. We made a conscious\nchoice not to add this for the following reasons:\n\n* Instagram is about your life on the go – we hope to encourage photos\n  from within the app.\n* We want to fight spam & low quality photos. Once we allow uploading\n  from other sources, it's harder to control what comes into the Instagram\n  ecosystem. All this being said, we're working on ways to ensure users\n  have a consistent and high-quality experience on our platform.\n"
        },
        {
            "name": "Commnts"
        },
        {
            "name": "Likes"
        },
        {
            "name": "Tags"
        },
        {
            "name": "Location"
        },
        {
            "name": "Subscribtions"
        }
    ],
    "securityDefinitions": {
        "oauth": {
            "type": "oauth2",
            "flow": "implicit",
            "authorizationUrl": "https://instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=token",
            "scopes": {
                "basic": "to read any and all data related to a user (e.g. following/followed-by\n lists, photos, etc.) (granted by default)\n",
                "comments": "to create or delete comments on a user’s behalf",
                "relationships": "to follow and unfollow users on a user’s behalf",
                "likes": "to like and unlike items on a user’s behalf"
            }
        },
        "key": {
            "type": "apiKey",
            "in": "query",
            "name": "access_token"
        }
    },
    "security": [
        {
            "oauth": [
                "basic",
                "comments",
                "relationships",
                "likes"
            ]
        },
        {
            "key": []
        }
    ],
    "parameters": {
        "user-id": {
            "name": "user-id",
            "in": "path",
            "description": "The user identifier number",
            "type": "number",
            "required": True
        },
        "tag-name": {
            "name": "tag-name",
            "in": "path",
            "description": "Tag name",
            "type": "string",
            "required": True
        }
    },
    "paths": {
        "/users/{user-id}": {
            "parameters": [
                {
                    "$ref": "#/parameters/user-id"
                }
            ],
            "get": {
                "security": [
                    {
                        "key": []
                    },
                    {
                        "oauth": [
                            "basic"
                        ]
                    }
                ],
                "tags": [
                    "Users"
                ],
                "description": "Get basic information about a user.",
                "responses": {
                    "200": {
                        "description": "The user object",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "$ref": "#/definitions/User"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/users/self/feed": {
            "get": {
                "tags": [
                    "Users"
                ],
                "description": "See the authenticated user's feed.",
                "parameters": [
                    {
                        "name": "count",
                        "in": "query",
                        "description": "Count of media to return.",
                        "type": "integer"
                    },
                    {
                        "name": "max_id",
                        "in": "query",
                        "description": "Return media earlier than this max_id.s",
                        "type": "integer"
                    },
                    {
                        "name": "min_id",
                        "in": "query",
                        "description": "Return media later than this min_id.",
                        "type": "integer"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Media"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/users/{user-id}/media/recent": {
            "parameters": [
                {
                    "$ref": "#/parameters/user-id"
                }
            ],
            "get": {
                "tags": [
                    "Users"
                ],
                "responses": {
                    "200": {
                        "description": "Get the most recent media published by a user. To get the most recent\nmedia published by the owner of the access token, you can use `self`\ninstead of the `user-id`.\n",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Media"
                                    }
                                }
                            }
                        }
                    }
                },
                "parameters": [
                    {
                        "name": "count",
                        "in": "query",
                        "description": "Count of media to return.",
                        "type": "integer"
                    },
                    {
                        "name": "max_timestamp",
                        "in": "query",
                        "description": "Return media before this UNIX timestamp.",
                        "type": "integer"
                    },
                    {
                        "name": "min_timestamp",
                        "in": "query",
                        "description": "Return media after this UNIX timestamp.",
                        "type": "integer"
                    },
                    {
                        "name": "min_id",
                        "in": "query",
                        "description": "Return media later than this min_id.",
                        "type": "string"
                    },
                    {
                        "name": "max_id",
                        "in": "query",
                        "description": "Return media earlier than this max_id.",
                        "type": "string"
                    }
                ]
            }
        },
        "/users/self/media/liked": {
            "get": {
                "tags": [
                    "Users"
                ],
                "description": "See the list of media liked by the authenticated user.\nPrivate media is returned as long as the authenticated user\nhas permissionto view that media. Liked media lists are only\navailable for the currently authenticated user.\n",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Media"
                                    }
                                }
                            }
                        }
                    }
                },
                "parameters": [
                    {
                        "name": "count",
                        "in": "query",
                        "description": "Count of media to return.",
                        "type": "integer"
                    },
                    {
                        "name": "max_like_id",
                        "in": "query",
                        "description": "Return media liked before this id.",
                        "type": "integer"
                    }
                ]
            }
        },
        "/users/search": {
            "get": {
                "tags": [
                    "Users"
                ],
                "description": "Search for a user by name.",
                "parameters": [
                    {
                        "name": "q",
                        "in": "query",
                        "description": "A query string",
                        "type": "string",
                        "required": True
                    },
                    {
                        "name": "count",
                        "in": "query",
                        "description": "Number of users to return.",
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/MiniProfile"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/users/{user-id}/follows": {
            "parameters": [
                {
                    "$ref": "#/parameters/user-id"
                }
            ],
            "get": {
                "tags": [
                    "Relationships"
                ],
                "description": "Get the list of users this user follows.",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/MiniProfile"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/users/{user-id}/followed-by": {
            "parameters": [
                {
                    "$ref": "#/parameters/user-id"
                }
            ],
            "get": {
                "tags": [
                    "Relationships"
                ],
                "description": "Get the list of users this user is followed by.",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/MiniProfile"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/users/self/requested-by": {
            "get": {
                "tags": [
                    "Relationships"
                ],
                "description": "List the users who have requested this user's permission to follow.\n",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "properties": {
                                "meta": {
                                    "properties": {
                                        "code": {
                                            "type": "integer"
                                        }
                                    }
                                },
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/MiniProfile"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/users/{user-id}/relationship": {
            "parameters": [
                {
                    "$ref": "#/parameters/user-id"
                }
            ],
            "post": {
                "tags": [
                    "Relationships"
                ],
                "description": "Modify the relationship between the current user and thetarget user.\n",
                "security": [
                    {
                        "oauth": [
                            "relationships"
                        ]
                    }
                ],
                "parameters": [
                    {
                        "name": "action",
                        "in": "body",
                        "description": "One of follow/unfollow/block/unblock/approve/ignore.",
                        "schema": {
                            "type": "string",
                            "enum": [
                                "follow",
                                "unfollow",
                                "block",
                                "unblock",
                                "approve"
                            ]
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/MiniProfile"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/media/{media-id}": {
            "parameters": [
                {
                    "name": "media-id",
                    "in": "path",
                    "description": "The media ID",
                    "type": "integer",
                    "required": True
                }
            ],
            "get": {
                "tags": [
                    "Media"
                ],
                "description": "Get information about a media object.\nThe returned type key will allow you to differentiate between `image`\nand `video` media.\n\nNote: if you authenticate with an OAuth Token, you will receive the\n`user_has_liked` key which quickly tells you whether the current user\nhas liked this media item.\n",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/Media"
                        }
                    }
                }
            }
        },
        "/media1/{shortcode}": {
            "parameters": [
                {
                    "name": "shortcode",
                    "in": "path",
                    "description": "The media shortcode",
                    "type": "string",
                    "required": True
                }
            ],
            "get": {
                "tags": [
                    "Media"
                ],
                "description": "This endpoint returns the same response as **GET** `/media/media-id`.\n\nA media object's shortcode can be found in its shortlink URL.\nAn example shortlink is `http://instagram.com/p/D/`\nIts corresponding shortcode is D.\n",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/Media"
                        }
                    }
                }
            }
        },
        "/media/search": {
            "get": {
                "tags": [
                    "Media"
                ],
                "description": "Search for media in a given area. The default time span is set to 5\ndays. The time span must not exceed 7 days. Defaults time stamps cover\nthe last 5 days. Can return mix of image and video types.\n",
                "parameters": [
                    {
                        "name": "LAT",
                        "description": "Latitude of the center search coordinate. If used, lng is required.\n",
                        "type": "number",
                        "in": "query"
                    },
                    {
                        "name": "MIN_TIMESTAMP",
                        "description": "A unix timestamp. All media returned will be taken later than\nthis timestamp.\n",
                        "type": "integer",
                        "in": "query"
                    },
                    {
                        "name": "LNG",
                        "description": "Longitude of the center search coordinate. If used, lat is required.\n",
                        "type": "number",
                        "in": "query"
                    },
                    {
                        "name": "MAX_TIMESTAMP",
                        "description": "A unix timestamp. All media returned will be taken earlier than this\ntimestamp.\n",
                        "type": "integer",
                        "in": "query"
                    },
                    {
                        "name": "DISTANCE",
                        "description": "Default is 1km (distance=1000), max distance is 5km.",
                        "type": "integer",
                        "maximum": 5000,
                        "default": 1000,
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "description": "List of all media with added `distance` property",
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "allOf": [
                                            {
                                                "$ref": "#/definitions/Media"
                                            },
                                            {
                                                "properties": {
                                                    "distance": {
                                                        "type": "number"
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/media/popular": {
            "get": {
                "tags": [
                    "Media"
                ],
                "description": "Get a list of what media is most popular at the moment.\nCan return mix of image and video types.\n",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Media"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/media/{media-id}/comments": {
            "parameters": [
                {
                    "name": "media-id",
                    "in": "path",
                    "description": "Media ID",
                    "type": "integer",
                    "required": True
                }
            ],
            "get": {
                "tags": [
                    "Comments"
                ],
                "description": "Get a list of recent comments on a media object.\n",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "properties": {
                                "meta": {
                                    "properties": {
                                        "code": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Comment"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": [
                    "Comments",
                    "Media"
                ],
                "description": "Create a comment on a media object with the following rules:\n\n* The total length of the comment cannot exceed 300 characters.\n* The comment cannot contain more than 4 hashtags.\n* The comment cannot contain more than 1 URL.\n* The comment cannot consist of all capital letters.\n",
                "security": [
                    {
                        "oauth": [
                            "comments"
                        ]
                    }
                ],
                "parameters": [
                    {
                        "name": "TEXT",
                        "description": "Text to post as a comment on the media object as specified in\nmedia-id.\n",
                        "in": "body",
                        "schema": {
                            "type": "number"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "meta": {
                                    "properties": {
                                        "code": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "data": {
                                    "type": "object"
                                }
                            }
                        }
                    }
                }
            },
            "delete": {
                "tags": [
                    "Comments"
                ],
                "description": "Remove a comment either on the authenticated user's media object or\nauthored by the authenticated user.\n",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "meta": {
                                    "properties": {
                                        "code": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "data": {
                                    "type": "object"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/media/{media-id}/likes": {
            "parameters": [
                {
                    "name": "media-id",
                    "in": "path",
                    "description": "Media ID",
                    "type": "integer",
                    "required": True
                }
            ],
            "get": {
                "tags": [
                    "Likes",
                    "Media"
                ],
                "description": "Get a list of users who have liked this media.\n",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "properties": {
                                "meta": {
                                    "properties": {
                                        "code": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Like"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": [
                    "Likes"
                ],
                "description": "Set a like on this media by the currently authenticated user.",
                "security": [
                    {
                        "oauth": [
                            "comments"
                        ]
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "meta": {
                                    "properties": {
                                        "code": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "data": {
                                    "type": "object"
                                }
                            }
                        }
                    }
                }
            },
            "delete": {
                "tags": [
                    "Likes"
                ],
                "description": "Remove a like on this media by the currently authenticated user.\n",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "meta": {
                                    "properties": {
                                        "code": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "data": {
                                    "type": "object"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/tags/{tag-name}": {
            "parameters": [
                {
                    "$ref": "#/parameters/tag-name"
                }
            ],
            "get": {
                "tags": [
                    "Tags"
                ],
                "description": "Get information about a tag object.",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/Tag"
                        }
                    }
                }
            }
        },
        "/tags/{tag-name}/media/recent": {
            "parameters": [
                {
                    "$ref": "#/parameters/tag-name"
                }
            ],
            "get": {
                "tags": [
                    "Tags"
                ],
                "description": "Get a list of recently tagged media. Use the `max_tag_id` and\n`min_tag_id` parameters in the pagination response to paginate through\nthese objects.\n",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Tag"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/tags/search": {
            "get": {
                "tags": [
                    "Tags"
                ],
                "parameters": [
                    {
                        "name": "q",
                        "description": "A valid tag name without a leading #. (eg. snowy, nofilter)\n",
                        "in": "query",
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "meta": {
                                    "properties": {
                                        "code": {
                                            "type": "integer"
                                        }
                                    }
                                },
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Tag"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/locations/{location-id}": {
            "parameters": [
                {
                    "name": "location-id",
                    "description": "Location ID",
                    "in": "path",
                    "type": "integer",
                    "required": True
                }
            ],
            "get": {
                "tags": [
                    "Location"
                ],
                "description": "Get information about a location.",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "$ref": "#/definitions/Location"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/locations/{location-id}/media/recent": {
            "parameters": [
                {
                    "name": "location-id",
                    "description": "Location ID",
                    "in": "path",
                    "type": "integer",
                    "required": True
                }
            ],
            "get": {
                "tags": [
                    "Location",
                    "Media"
                ],
                "description": "Get a list of recent media objects from a given location.",
                "parameters": [
                    {
                        "name": "max_timestamp",
                        "in": "query",
                        "description": "Return media before this UNIX timestamp.",
                        "type": "integer"
                    },
                    {
                        "name": "min_timestamp",
                        "in": "query",
                        "description": "Return media after this UNIX timestamp.",
                        "type": "integer"
                    },
                    {
                        "name": "min_id",
                        "in": "query",
                        "description": "Return media later than this min_id.",
                        "type": "string"
                    },
                    {
                        "name": "max_id",
                        "in": "query",
                        "description": "Return media earlier than this max_id.",
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Media"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/locations/search": {
            "get": {
                "tags": [
                    "Location"
                ],
                "description": "Search for a location by geographic coordinate.",
                "parameters": [
                    {
                        "name": "distance",
                        "in": "query",
                        "description": "Default is 1000m (distance=1000), max distance is 5000.",
                        "type": "integer"
                    },
                    {
                        "name": "facebook_places_id",
                        "in": "query",
                        "description": "Returns a location mapped off of a Facebook places id. If used, a\nFoursquare id and lat, lng are not required.\n",
                        "type": "integer"
                    },
                    {
                        "name": "foursquare_id",
                        "in": "query",
                        "description": "returns a location mapped off of a foursquare v1 api location id.\nIf used, you are not required to use lat and lng. Note that this\nmethod is deprecated; you should use the new foursquare IDs with V2\nof their API.\n",
                        "type": "integer"
                    },
                    {
                        "name": "lat",
                        "in": "query",
                        "description": "atitude of the center search coordinate. If used, lng is required.\n",
                        "type": "number"
                    },
                    {
                        "name": "lng",
                        "in": "query",
                        "description": "ongitude of the center search coordinate. If used, lat is required.\n",
                        "type": "number"
                    },
                    {
                        "name": "foursquare_v2_id",
                        "in": "query",
                        "description": "Returns a location mapped off of a foursquare v2 api location id. If\nused, you are not required to use lat and lng.\n",
                        "type": "integer"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Location"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/geographies/{geo-id}/media/recent": {
            "parameters": [
                {
                    "name": "geo-id",
                    "in": "path",
                    "description": "Geolocation ID",
                    "type": "integer",
                    "required": True
                }
            ],
            "get": {
                "description": "Get recent media from a geography subscription that you created.\n**Note**: You can only access Geographies that were explicitly created\nby your OAuth client. Check the Geography Subscriptions section of the\n[real-time updates page](https://instagram.com/developer/realtime/).\nWhen you create a subscription to some geography\nthat you define, you will be returned a unique geo-id that can be used\nin this query. To backfill photos from the location covered by this\ngeography, use the [media search endpoint\n](https://instagram.com/developer/endpoints/media/).\n",
                "parameters": [
                    {
                        "name": "count",
                        "in": "query",
                        "description": "Max number of media to return.",
                        "type": "integer"
                    },
                    {
                        "name": "min_id",
                        "in": "query",
                        "description": "Return media before this `min_id`.",
                        "type": "integer"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK"
                    }
                }
            }
        }
    },
    "definitions": {
        "User": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "username": {
                    "type": "string"
                },
                "full_name": {
                    "type": "string"
                },
                "profile_picture": {
                    "type": "string"
                },
                "bio": {
                    "type": "string"
                },
                "website": {
                    "type": "string"
                },
                "counts": {
                    "type": "object",
                    "properties": {
                        "media": {
                            "type": "integer"
                        },
                        "follows": {
                            "type": "integer"
                        },
                        "follwed_by": {
                            "type": "integer"
                        }
                    }
                }
            }
        },
        "Media": {
            "type": "object",
            "properties": {
                "created_time": {
                    "description": "Epoc time (ms)",
                    "type": "integer"
                },
                "type": {
                    "type": "string"
                },
                "filter": {
                    "type": "string"
                },
                "tags": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Tag"
                    }
                },
                "id": {
                    "type": "integer"
                },
                "user": {
                    "$ref": "#/definitions/MiniProfile"
                },
                "users_in_photo": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/MiniProfile"
                    }
                },
                "location": {
                    "$ref": "#/definitions/Location"
                },
                "comments:": {
                    "type": "object",
                    "properties": {
                        "count": {
                            "type": "integer"
                        },
                        "data": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/Comment"
                            }
                        }
                    }
                },
                "likes": {
                    "type": "object",
                    "properties": {
                        "count": {
                            "type": "integer"
                        },
                        "data": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/MiniProfile"
                            }
                        }
                    }
                },
                "images": {
                    "properties": {
                        "low_resolution": {
                            "$ref": "#/definitions/Image"
                        },
                        "thumbnail": {
                            "$ref": "#/definitions/Image"
                        },
                        "standard_resolution": {
                            "$ref": "#/definitions/Image"
                        }
                    }
                },
                "videos": {
                    "properties": {
                        "low_resolution": {
                            "$ref": "#/definitions/Image"
                        },
                        "standard_resolution": {
                            "$ref": "#/definitions/Image"
                        }
                    }
                }
            }
        },
        "Location": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "latitude": {
                    "type": "number"
                },
                "longitude": {
                    "type": "number"
                }
            }
        },
        "Comment": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "created_time": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                },
                "from": {
                    "$ref": "#/definitions/MiniProfile"
                }
            }
        },
        "Like": {
            "type": "object",
            "properties": {
                "user_name": {
                    "type": "string"
                },
                "first_name": {
                    "type": "string"
                },
                "last_name": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "id": {
                    "type": "string"
                }
            }
        },
        "Tag": {
            "type": "object",
            "properties": {
                "media_count": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            }
        },
        "Image": {
            "type": "object",
            "properties": {
                "width": {
                    "type": "integer"
                },
                "height": {
                    "type": "integer"
                },
                "url": {
                    "type": "string"
                }
            }
        },
        "MiniProfile": {
            "type": "object",
            "description": "A shorter version of User for likes array",
            "properties": {
                "user_name": {
                    "type": "string"
                },
                "full_name": {
                    "type": "string"
                },
                "id": {
                    "type": "integer"
                },
                "profile_picture": {
                    "type": "string"
                }
            }
        }
    }
}
