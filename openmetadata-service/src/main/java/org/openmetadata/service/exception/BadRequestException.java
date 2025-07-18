/*
 *  Copyright 2021 Collate
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *  http://www.apache.org/licenses/LICENSE-2.0
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

package org.openmetadata.service.exception;

import jakarta.ws.rs.core.Response;
import org.openmetadata.sdk.exception.WebServiceException;

public final class BadRequestException extends WebServiceException {
  private static final String DEFAULT_MESSAGE = "Bad request.";
  private static final String ERROR_TYPE = "BAD_REQUEST";

  private BadRequestException() {
    super(Response.Status.BAD_REQUEST, ERROR_TYPE, DEFAULT_MESSAGE);
  }

  public BadRequestException(String message) {
    super(Response.Status.BAD_REQUEST, ERROR_TYPE, message);
  }

  public static BadRequestException of() {
    return new BadRequestException();
  }

  public static BadRequestException of(String message) {
    return new BadRequestException(message);
  }
}
