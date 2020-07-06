from drf_yasg import openapi


parent_create_post = {
    'request_body': openapi.Schema(
        title='Parent',
        type=openapi.TYPE_OBJECT,
        properties={
            'user': openapi.Schema(
                title='User',
                type=openapi.TYPE_OBJECT,
                properties={
                    'phone': openapi.Schema(
                        description='전화번호 (- 없이 입력)',
                        type=openapi.TYPE_STRING,
                    ),
                    'password': openapi.Schema(
                        description='비밀번호',
                        type=openapi.TYPE_STRING,
                    ),
                    'password_check': openapi.Schema(
                        description='비밀번호 확인',
                        type=openapi.TYPE_STRING,
                    ),
                },
                required=['phone', 'password', 'password_check'],
            ),
            'name': openapi.Schema(
                description='이름',
                type=openapi.TYPE_STRING,
            ),
            'image': openapi.Schema(
                description='프로필 사진',
                type=openapi.TYPE_FILE,
            ),
        },
        required=['user', 'name'],
    ),
    'responses': {
        '201': openapi.Schema(
            title='Parent',
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    title='User',
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'phone': openapi.Schema(
                            description='전화번호 (- 없이 입력)',
                            type=openapi.TYPE_STRING,
                        ),
                    },
                ),
                'name': openapi.Schema(
                    description='이름',
                    type=openapi.TYPE_STRING,
                ),
                'image': openapi.Schema(
                    description='프로필 사진',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
        '400': openapi.Schema(
            title='Parent',
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    title='User',
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'phone': openapi.Schema(
                            description='ERROR: 전화번호',
                            type=openapi.TYPE_STRING,
                        ),
                        'password': openapi.Schema(
                            description='ERROR: 비밀번호',
                            type=openapi.TYPE_STRING,
                        ),
                        'password_check': openapi.Schema(
                            description='ERROR: 비밀번호 확인',
                            type=openapi.TYPE_STRING,
                        ),
                    },
                ),
                'name': openapi.Schema(
                    description='ERROR: 이름',
                    type=openapi.TYPE_STRING,
                ),
                'image': openapi.Schema(
                    description='ERROR: 프로필 사진',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
    },
}

student_create_post = {
    'request_body': openapi.Schema(
        title='Student',
        type=openapi.TYPE_OBJECT,
        properties={
            'user': openapi.Schema(
                title='User',
                type=openapi.TYPE_OBJECT,
                properties={
                    'phone': openapi.Schema(
                        description='전화번호 (- 없이 입력)',
                        type=openapi.TYPE_STRING,
                    ),
                    'password': openapi.Schema(
                        description='비밀번호',
                        type=openapi.TYPE_STRING,
                    ),
                    'password_check': openapi.Schema(
                        description='비밀번호 확인',
                        type=openapi.TYPE_STRING,
                    ),
                },
                required=['phone', 'password', 'password_check'],
            ),
            'name': openapi.Schema(
                description='이름',
                type=openapi.TYPE_STRING,
            ),
            'image': openapi.Schema(
                description='프로필 사진',
                type=openapi.TYPE_FILE,
            ),
            'parent_phone': openapi.Schema(
                description='학부모 전화번호',
                type=openapi.TYPE_STRING,
            ),
        },
        required=['user', 'name'],
    ),
    'responses': {
        '201': openapi.Schema(
            title='Student',
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    title='User',
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'phone': openapi.Schema(
                            description='전화번호 (- 없이 입력)',
                            type=openapi.TYPE_STRING,
                        ),
                    },
                ),
                'name': openapi.Schema(
                    description='이름',
                    type=openapi.TYPE_STRING,
                ),
                'image': openapi.Schema(
                    description='프로필 사진',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
        '400': openapi.Schema(
            title='Student',
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    title='User',
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'phone': openapi.Schema(
                            description='ERROR: 전화번호',
                            type=openapi.TYPE_STRING,
                        ),
                        'password': openapi.Schema(
                            description='ERROR: 비밀번호',
                            type=openapi.TYPE_STRING,
                        ),
                        'password_check': openapi.Schema(
                            description='ERROR: 비밀번호 확인',
                            type=openapi.TYPE_STRING,
                        ),
                    },
                ),
                'name': openapi.Schema(
                    description='ERROR: 이름',
                    type=openapi.TYPE_STRING,
                ),
                'image': openapi.Schema(
                    description='ERROR: 프로필 사진',
                    type=openapi.TYPE_STRING,
                ),
                'parent_phone': openapi.Schema(
                    description='ERROR: 학부모 전화번호',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
    },
}

teacher_create_post = {
    'request_body': openapi.Schema(
        title='Teacher',
        type=openapi.TYPE_OBJECT,
        properties={
            'user': openapi.Schema(
                title='User',
                type=openapi.TYPE_OBJECT,
                properties={
                    'phone': openapi.Schema(
                        description='전화번호 (- 없이 입력)',
                        type=openapi.TYPE_STRING,
                    ),
                    'password': openapi.Schema(
                        description='비밀번호',
                        type=openapi.TYPE_STRING,
                    ),
                    'password_check': openapi.Schema(
                        description='비밀번호 확인',
                        type=openapi.TYPE_STRING,
                    ),
                },
                required=['phone', 'password', 'password_check'],
            ),
            'name': openapi.Schema(
                description='이름',
                type=openapi.TYPE_STRING,
            ),
            'image': openapi.Schema(
                description='프로필 사진',
                type=openapi.TYPE_FILE,
            ),
            'academy_phone': openapi.Schema(
                description='학원 전화번호',
                type=openapi.TYPE_STRING,
            ),
        },
        required=['user', 'name', 'academy_phone'],
    ),
    'responses': {
        '201': openapi.Schema(
            title='Teacher',
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    title='User',
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'phone': openapi.Schema(
                            description='전화번호 (- 없이 입력)',
                            type=openapi.TYPE_STRING,
                        ),
                    },
                ),
                'name': openapi.Schema(
                    description='이름',
                    type=openapi.TYPE_STRING,
                ),
                'image': openapi.Schema(
                    description='프로필 사진',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
        '400': openapi.Schema(
            title='Teacher',
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    title='User',
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'phone': openapi.Schema(
                            description='ERROR: 전화번호',
                            type=openapi.TYPE_STRING,
                        ),
                        'password': openapi.Schema(
                            description='ERROR: 비밀번호',
                            type=openapi.TYPE_STRING,
                        ),
                        'password_check': openapi.Schema(
                            description='ERROR: 비밀번호 확인',
                            type=openapi.TYPE_STRING,
                        ),
                    },
                ),
                'name': openapi.Schema(
                    description='ERROR: 이름',
                    type=openapi.TYPE_STRING,
                ),
                'image': openapi.Schema(
                    description='ERROR: 프로필 사진',
                    type=openapi.TYPE_STRING,
                ),
                'academy_phone': openapi.Schema(
                    description='ERROR: 학원 전화번호',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
    },
}

parent_detail_get = {
    'manual_parameters': [
        openapi.Parameter(
            name='id',
            description='pk of a specific Parent object',
            in_=openapi.IN_PATH,
            type=openapi.TYPE_INTEGER,
        )
    ],
    'responses': {
        '200': openapi.Schema(
            title='Parent',
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    title='User',
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'phone': openapi.Schema(
                            description='전화번호',
                            type=openapi.TYPE_STRING,
                        ),
                    },
                ),
                'name': openapi.Schema(
                    description='이름',
                    type=openapi.TYPE_STRING,
                ),
                'image': openapi.Schema(
                    description='프로필 사진',
                    type=openapi.TYPE_STRING,
                ),
                'students': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        title='Student',
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'user': openapi.Schema(
                                title='User',
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'phone': openapi.Schema(
                                        description='전화번호',
                                        type=openapi.TYPE_STRING,
                                    ),
                                },
                            ),
                            'name': openapi.Schema(
                                description='이름',
                                type=openapi.TYPE_STRING,
                            ),
                            'image': openapi.Schema(
                                description='프로필 사진',
                                type=openapi.TYPE_STRING,
                            ),
                        },
                    ),
                ),
            },
        ),
        '404': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(
                    description='ERROR',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
    },
}

parent_detail_put = {
    'manual_parameters': [
        openapi.Parameter(
            name='id',
            description='pk of a specific Parent object',
            in_=openapi.IN_PATH,
            type=openapi.TYPE_INTEGER,
        )
    ],
    'request_body': openapi.Schema(
        title='Parent',
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(
                description='이름',
                type=openapi.TYPE_STRING,
            ),
            'image': openapi.Schema(
                description='프로필 사진',
                type=openapi.TYPE_FILE,
            ),
        },
        required=['user', 'name'],
    ),
    'responses': {
        '201': openapi.Schema(
            title='Parent',
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(
                    description='이름',
                    type=openapi.TYPE_STRING,
                ),
                'image': openapi.Schema(
                    description='프로필 사진',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
        '400': openapi.Schema(
            title='Parent',
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(
                    description='ERROR: 이름',
                    type=openapi.TYPE_STRING,
                ),
                'image': openapi.Schema(
                    description='ERROR: 프로필 사진',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
    },
}

parent_detail_delete = {
    'manual_parameters': [
        openapi.Parameter(
            name='id',
            description='pk of a specific Parent object',
            in_=openapi.IN_PATH,
            type=openapi.TYPE_INTEGER,
        )
    ],
    'responses': {
        '204': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'success': openapi.Schema(
                    description='SUCCESS',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
        '404': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(
                    description='ERROR',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
    },
}

student_detail_get = {
    'manual_parameters': [
        openapi.Parameter(
            name='id',
            description='pk of a specific Student object',
            in_=openapi.IN_PATH,
            type=openapi.TYPE_INTEGER,
        )
    ],
    'responses': {
        '200': openapi.Schema(
            title='Student',
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(
                    title='User',
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'phone': openapi.Schema(
                            description='전화번호',
                            type=openapi.TYPE_STRING,
                        ),
                    },
                ),
                'name': openapi.Schema(
                    description='이름',
                    type=openapi.TYPE_STRING,
                ),
                'image': openapi.Schema(
                    description='프로필 사진',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
        '404': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(
                    description='ERROR',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
    },
}

student_detail_put = {
    'manual_parameters': [
        openapi.Parameter(
            name='id',
            description='pk of a specific Student object',
            in_=openapi.IN_PATH,
            type=openapi.TYPE_INTEGER,
        )
    ],
    'request_body': openapi.Schema(
        title='Student',
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(
                description='이름',
                type=openapi.TYPE_STRING,
            ),
            'image': openapi.Schema(
                description='프로필 사진',
                type=openapi.TYPE_FILE,
            ),
        },
        required=['user', 'name'],
    ),
    'responses': {
        '201': openapi.Schema(
            title='Student',
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(
                    description='이름',
                    type=openapi.TYPE_STRING,
                ),
                'image': openapi.Schema(
                    description='프로필 사진',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
        '400': openapi.Schema(
            title='Student',
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(
                    description='ERROR: 이름',
                    type=openapi.TYPE_STRING,
                ),
                'image': openapi.Schema(
                    description='ERROR: 프로필 사진',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
    },
}

student_detail_delete = {
    'manual_parameters': [
        openapi.Parameter(
            name='id',
            description='pk of a specific Student object',
            in_=openapi.IN_PATH,
            type=openapi.TYPE_INTEGER,
        )
    ],
    'responses': {
        '204': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'success': openapi.Schema(
                    description='SUCCESS',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
        '404': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'error': openapi.Schema(
                    description='ERROR',
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
    },
}

