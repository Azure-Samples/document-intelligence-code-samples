// coding: utf - 8
// --------------------------------------------------------------------------
// Copyright(c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
// --------------------------------------------------------------------------
using Azure.AI.DocumentIntelligence;

namespace Quickstarts
{
    public static class SdkExtension
    {
        /// <summary>
        /// Parse the BoundingRegion to coordinate boundary
        /// </summary>
        /// <param name="boundingRegion">BoundingRegion</param>
        /// <returns> the important coordinate boundary </returns>
        public static (float, float, float, float) CoordinateBoundary(this BoundingRegion boundingRegion)
        {
            // To learn more about bounding regions, see https://aka.ms/bounding-region
            var x_left = boundingRegion.Polygon[0];
            var y_top = boundingRegion.Polygon[1];
            var x_right = boundingRegion.Polygon[4];
            var y_bottom = boundingRegion.Polygon[5];

            return (x_left, y_top, x_right, y_bottom);
        }
    }
}
