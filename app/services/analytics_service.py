from collections import Counter

from app.database.supabase_client import supabase


class AnalyticsService:

    @staticmethod
    def top_cars():

        builds = (
            supabase.table("builds")
            .select("stock_car_id")
            .execute()
            .data
        )

        counter = Counter(
            build["stock_car_id"]
            for build in builds
        )

        top = counter.most_common(5)

        result = []

        for car_id, total in top:

            car = (
                supabase.table("stock_cars")
                .select("brand, model")
                .eq("id", car_id)
                .execute()
                .data[0]
            )

            result.append({
                "name": f"{car['brand']} {car['model']}",
                "total": total
            })

        return result

    @staticmethod
    def top_mods():

        mods = (
            supabase.table("build_mods")
            .select("mod_id")
            .execute()
            .data
        )

        counter = Counter(
            mod["mod_id"]
            for mod in mods
        )

        top = counter.most_common(5)

        result = []

        for mod_id, total in top:

            mod = (
                supabase.table("mods")
                .select("name")
                .eq("id", mod_id)
                .execute()
                .data[0]
            )

            result.append({
                "name": mod["name"],
                "total": total
            })

        return result

    @staticmethod
    def expensive_builds():

        builds = (
            supabase.table("builds")
            .select("*")
            .order(
                "price",
                desc=True
            )
            .limit(5)
            .execute()
            .data
        )

        return [
            {
                "name": build["build_name"],
                "price": build["price"]
            }
            for build in builds
        ]

    @staticmethod
    def build_approach_stats():

        builds = (
            supabase.table("builds")
            .select("build_approach")
            .execute()
            .data
        )

        total = len(builds)

        counter = Counter(
            build["build_approach"]
            for build in builds
        )

        return [
            {
                "approach": name,
                "percentage": round(
                    count * 100 / total,
                    2
                )
            }
            for name, count in counter.items()
        ]

    @staticmethod
    def fuel_type_stats():

        builds = (
            supabase.table("builds")
            .select("stock_car_id")
            .execute()
            .data
        )

        fuels = []

        for build in builds:

            car = (
                supabase.table("stock_cars")
                .select("fuel")
                .eq(
                    "id",
                    build["stock_car_id"]
                )
                .execute()
                .data[0]
            )

            fuels.append(
                car["fuel"]
            )

        total = len(fuels)

        counter = Counter(fuels)

        return [
            {
                "fuel": fuel,
                "percentage": round(
                    count * 100 / total,
                    2
                )
            }
            for fuel, count in counter.items()
        ]