/*
 * Copyright 2017-2018 Tom van Dijk, Johannes Kepler University Linz
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/*
 * Derived from Oink (https://github.com/trolando/oink) and Vanessa Flügel's
 * fork (https://github.com/vfluegel/oink). This file is licensed under
 * Apache-2.0 rather than the repository's MIT license. Apache-2.0 → MIT
 * relicensing requires the copyright holders' consent; until that consent
 * is obtained this file remains Apache-2.0.
 * Changes: ported to C23 and modified for tree output.
 */

#include "pm_internal.h"

void sspm_truncate(PMMeasure *measure, int const pindex) {
  if (measure->top) {
    return;
  }
  for (int i = measure->length - 1; i >= 0 && measure->levels[i] > pindex;
       i--) {
    measure->bits[i] = 0;
    measure->levels[i] = pindex + 1;
  }
}

void sspm_successor(PMMeasure *measure, int const pindex, int const depth) {
  if (measure->top) {
    return;
  }
  int const length = measure->length;
  if (length == 0) {
    measure->top = true;
    return;
  }
  if (measure->levels[length - 1] > pindex) {
    int i = length - 1;
    for (; i >= 0 && measure->levels[i] > pindex; i--) {
      measure->bits[i] = 0;
      measure->levels[i] = pindex;
    }
    measure->bits[i + 1] = 1;
    return;
  }
  for (int i = length - 1; i >= 0; i--) {
    if (measure->bits[i] == 0) {
      if (measure->levels[i] == depth) {
        measure->bits[i] = 1;
      } else {
        int const level = measure->levels[i] + 1;
        for (int j = i; j < length; j++) {
          measure->levels[j] = level;
        }
      }
      break;
    }
    if (i == 0 && measure->levels[0] == 0) {
      measure->top = true;
      break;
    }
    if (i == 0 || measure->levels[i - 1] != measure->levels[i]) {
      int const level = measure->levels[i] - 1;
      measure->bits[i] = 1;
      for (int j = i; j < length; j++) {
        measure->levels[j] = level;
      }
      break;
    }
    measure->bits[i] = 0;
  }
}
