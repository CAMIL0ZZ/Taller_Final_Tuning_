from app.database.supabase_client import supabase


class AnalyticsService:

    @staticmethod
    def top_cars():

        return (
            supabase.table("builds")
            .select("stock_car_id")
            .execute()
            .data
        )

    @staticmethod
    def top_mods():

        return (
            supabase.table("build_mods")
            .select("mod_id")
            .execute()
            .data
        )

    @staticmethod
    def expensive_builds():

        return (
            supabase.table("builds")
            .select("*")
            .order("price", desc=True)
            .limit(10)
            .execute()
            .data
        )

    @staticmethod
    def build_approach_stats():

        return (
            supabase.table("builds")
            .select("build_approach")
            .execute()
            .data
        )