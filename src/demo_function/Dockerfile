# Base Image for Lambda Functions
FROM public.ecr.aws/lambda/python:3.9

# Install python poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
RUN poetry config virtualenvs.create false

# Copy the poetry files to Docker image
COPY poetry.lock pyproject.toml ./

# Extract dependencies from poetry.lock and install them with pip
RUN poetry export --format requirements.txt --without-hashes --output requirements.txt
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY ${RESOLVER_NAME}/ ${LAMBDA_TASK_ROOT}/${RESOLVER_NAME}

# Set the CMD to your handler
CMD [ "demo_function.index.lambda_handler" ]
